import sqlite3
import pandas as pd

# Configuration
DATABASE = 'movies.db'
CSV_FILE = 'movies.csv'  # Ensure this CSV is placed in the same directory

def create_tables(conn):
    cursor = conn.cursor()
    # Drop existing tables if necessary
    cursor.execute('DROP TABLE IF EXISTS movies')
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('DROP TABLE IF EXISTS preferences')

    # Create movies table
    cursor.execute('''
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Series_Title TEXT NOT NULL,
            Released_Year INTEGER,
            Certificate TEXT,
            Runtime TEXT,
            Genre TEXT,
            IMDB_Rating REAL,
            Overview TEXT,
            Meta_score INTEGER,
            Director TEXT,
            Star1 TEXT,
            Star2 TEXT,
            Star3 TEXT,
            Star4 TEXT,
            No_of_Votes INTEGER,
            Gross INTEGER,
            Poster_Link TEXT
        )
    ''')

    # Create users table
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Create preferences table
    cursor.execute('''
        CREATE TABLE preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            genres TEXT,
            min_year INTEGER,
            max_year INTEGER,
            min_rating REAL,
            director TEXT,
            sort_by TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()

def import_movies(conn):
    df = pd.read_csv(CSV_FILE)

    # Data cleaning
    df = df.dropna(subset=['Series_Title', 'Released_Year', 'Genre', 'IMDB_Rating'])
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce').fillna(0).astype(int)
    df['IMDB_Rating'] = pd.to_numeric(df['IMDB_Rating'], errors='coerce').fillna(0)
    df['Meta_score'] = pd.to_numeric(df['Meta_score'], errors='coerce')
    df['No_of_Votes'] = pd.to_numeric(df['No_of_Votes'], errors='coerce').fillna(0).astype(int)
    df['Gross'] = df['Gross'].replace(',', '', regex=True)
    df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce').fillna(0).astype(int)

    # Insert data into movies table
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO movies (
                Series_Title, Released_Year, Certificate, Runtime, Genre,
                IMDB_Rating, Overview, Meta_score, Director, Star1, Star2, Star3, Star4,
                No_of_Votes, Gross, Poster_Link
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['Series_Title'], row['Released_Year'], row['Certificate'], row['Runtime'], row['Genre'],
            row['IMDB_Rating'], row['Overview'], row['Meta_score'], row['Director'], row['Star1'],
            row['Star2'], row['Star3'], row['Star4'], row['No_of_Votes'], row['Gross'], row['Poster_Link']
        ))

    conn.commit()
    print("Movies imported successfully.")

def main():
    conn = sqlite3.connect(DATABASE)
    create_tables(conn)
    import_movies(conn)
    conn.close()

if __name__ == '__main__':
    main()
