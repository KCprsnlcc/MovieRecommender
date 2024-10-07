from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

DATABASE = 'movies.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Retrieve user preferences if any
    cursor.execute("SELECT * FROM preferences WHERE user_id = ?", (session['user_id'],))
    pref = cursor.fetchone()

    # Retrieve genres and directors for the dropdown
    cursor.execute("SELECT DISTINCT Genre FROM movies")
    genres_data = cursor.fetchall()
    genre_set = set()
    for row in genres_data:
        genres = row['Genre'].split(',')
        for genre in genres:
            genre_set.add(genre.strip())
    genres = sorted(list(genre_set))

    cursor.execute("SELECT DISTINCT Director FROM movies")
    directors_data = cursor.fetchall()
    directors = sorted([row['Director'] for row in directors_data if row['Director']])

    movies = None
    if pref:
        # Use saved preferences
        selected_genres = pref['genres'].split(',') if pref['genres'] else []
        min_year = pref['min_year'] if pref['min_year'] else 1900
        max_year = pref['max_year'] if pref['max_year'] else 2024
        min_rating = pref['min_rating'] if pref['min_rating'] else 0
        selected_director = pref['director'] if pref['director'] else ''
        sort_by = pref['sort_by'] if pref['sort_by'] else 'rating_desc'
    else:
        # Default preferences
        selected_genres = []
        min_year = 1900
        max_year = 2024
        min_rating = 0
        selected_director = ''
        sort_by = 'rating_desc'

    if request.method == 'POST':
        # Update preferences based on form input
        selected_genres = request.form.getlist('genres')
        min_year = request.form.get('min_year', 1900)
        max_year = request.form.get('max_year', 2024)
        min_rating = request.form.get('min_rating', 0)
        selected_director = request.form.get('director', '')
        sort_by = request.form.get('sort_by', 'rating_desc')

        # Save preferences to the database
        genres_str = ','.join(selected_genres)
        cursor.execute("SELECT * FROM preferences WHERE user_id = ?", (session['user_id'],))
        existing_pref = cursor.fetchone()
        if existing_pref:
            cursor.execute('''
                UPDATE preferences
                SET genres = ?, min_year = ?, max_year = ?, min_rating = ?, director = ?, sort_by = ?
                WHERE user_id = ?
            ''', (genres_str, min_year, max_year, min_rating, selected_director, sort_by, session['user_id']))
        else:
            cursor.execute('''
                INSERT INTO preferences (user_id, genres, min_year, max_year, min_rating, director, sort_by)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (session['user_id'], genres_str, min_year, max_year, min_rating, selected_director, sort_by))
        conn.commit()

    # Build the query based on preferences
    query = "SELECT * FROM movies WHERE 1=1"
    params = []

    if selected_genres:
        genre_conditions = " OR ".join(["Genre LIKE ?"] * len(selected_genres))
        query += f" AND ({genre_conditions})"
        for genre in selected_genres:
            params.append(f"%{genre}%")
    if min_year:
        query += " AND Released_Year >= ?"
        params.append(min_year)
    if max_year:
        query += " AND Released_Year <= ?"
        params.append(max_year)
    if min_rating:
        query += " AND IMDB_Rating >= ?"
        params.append(min_rating)
    if selected_director:
        query += " AND Director = ?"
        params.append(selected_director)

    # Sorting
    if sort_by == 'rating_desc':
        query += " ORDER BY IMDB_Rating DESC, Released_Year DESC"
    elif sort_by == 'rating_asc':
        query += " ORDER BY IMDB_Rating ASC, Released_Year ASC"
    elif sort_by == 'year_desc':
        query += " ORDER BY Released_Year DESC, IMDB_Rating DESC"
    elif sort_by == 'year_asc':
        query += " ORDER BY Released_Year ASC, IMDB_Rating ASC"
    
    query += " LIMIT 20"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    movies = [dict(row) for row in rows]

    return render_template('index.html', genres=genres, directors=directors, movies=movies,
                           selected_genres=selected_genres,
                           min_year=min_year,
                           max_year=max_year,
                           min_rating=min_rating,
                           selected_director=selected_director,
                           sort_by=sort_by)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not username or not password:
            flash("Username and password are required.", "danger")
            return redirect(url_for('register'))
        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (username, password)
                VALUES (?, ?)
            ''', (username, hashed_password))
            conn.commit()
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Please choose a different one.", "danger")
            return redirect(url_for('register'))
        finally:
            conn.close()
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash("Logged in successfully.", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
