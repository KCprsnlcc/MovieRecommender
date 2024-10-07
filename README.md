# Movie Recommender System

A **Movie Recommender System** built with **Python Flask**, **SQLite**, and **Bootstrap**. This application allows users to register, set their movie preferences, and receive personalized movie recommendations. Users can also rate movies, add them to their favorites list, and browse movies with features like pagination and real-time search filtering.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **User Authentication**: Secure registration and login system.
- **User Preferences**: Users can set preferences like genres, release year range, minimum IMDB rating, and director.
- **Movie Recommendations**: Personalized recommendations based on user preferences.
- **Pagination**: Efficient navigation through multiple pages of movie recommendations with truncated pagination controls.
- **Real-time Search Filtering**: Instant filtering of displayed movies as the user types.
- **User Ratings**: Users can rate movies, and these ratings are stored for personalized recommendations.
- **Favorites List**: Users can add movies to a favorites list for easy access.
- **Detailed Movie Pages**: View detailed information about each movie, including overview, cast, and user rating.
- **Responsive Design**: Sleek and minimalistic flat UI design with responsive elements for different screen sizes.

---

## Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package installer)
- **Git** (optional, for cloning the repository)

---

## Installation

### 1. Clone the Repository

You can clone this repository using Git or download the ZIP file.

```bash
git clone https://github.com/KCprsnlcc/MovieRecommender.git
cd MovieRecommender
```

### 2. Set Up a Python Virtual Environment

It is recommended to use a virtual environment to manage dependencies. You can use `venv`, which comes with Python 3.

#### On Windows:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

#### On macOS and Linux:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

*If `requirements.txt` does not exist, create it with the following content:*

```text
Flask
Werkzeug
pandas
```

Install the packages:

```bash
pip install Flask Werkzeug pandas
```

### 4. Prepare the Dataset

Place your `movies.csv` file in the project directory. Ensure the CSV file is properly formatted with the following columns:

- `Poster_Link`
- `Series_Title`
- `Released_Year`
- `Certificate`
- `Runtime`
- `Genre`
- `IMDB_Rating`
- `Overview`
- `Meta_score`
- `Director`
- `Star1`
- `Star2`
- `Star3`
- `Star4`
- `No_of_Votes`
- `Gross`

*Example of `movies.csv`:*

```csv
Poster_Link,Series_Title,Released_Year,Certificate,Runtime,Genre,IMDB_Rating,Overview,Meta_score,Director,Star1,Star2,Star3,Star4,No_of_Votes,Gross
https://link1.jpg,The Shawshank Redemption,1994,A,142 min,Drama,9.3,"Two imprisoned men bond over a number of years...",80,Frank Darabont,Tim Robbins,Morgan Freeman,Bob Gunton,William Sadler,2343110,28341469
https://link2.jpg,The Godfather,1972,A,175 min,Crime, Drama,9.2,"An organized crime dynasty's aging patriarch...",100,Francis Ford Coppola,Marlon Brando,Al Pacino,James Caan,Diane Keaton,1620367,134966411
```

### 5. Import the Data

Run the `import_data.py` script to create the SQLite database and import the movie data.

```bash
python import_data.py
```

---

## Running the Application

With the virtual environment activated and dependencies installed, you can run the Flask application.

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`. Open this URL in your web browser to access the application.

---

## Usage

1. **Register**: Create a new user account by clicking on the "Register" link.
2. **Login**: Log in with your username and password.
3. **Set Preferences**: On the home page, set your movie preferences and click "Get Recommendations".
4. **Browse Movies**: View recommended movies, use pagination controls to navigate, and search to filter movies.
5. **View Details**: Click on a movie to view detailed information.
6. **Rate Movies**: Rate movies on their detail pages.
7. **Manage Favorites**: Add movies to your favorites list for easy access.
8. **Logout**: Click "Logout" in the navigation bar to end your session.

---

## Project Structure

```
movie_recommender_system/
│
├── app.py                   # Main Flask application
├── import_data.py           # Script to import movie data into SQLite database
├── movies.db                # SQLite database file (created after running import_data.py)
├── movies.csv               # CSV file containing movie data (you need to provide this)
├── requirements.txt         # Python dependencies
├── templates/
│   ├── base.html            # Base HTML template
│   ├── index.html           # Home page template
│   ├── login.html           # Login page template
│   ├── register.html        # Registration page template
│   ├── favorites.html       # Favorites page template
│   └── movie_detail.html    # Movie detail page template
└── static/
    ├── styles.css           # CSS styles
    └── scripts.js           # JavaScript scripts
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# Instructions for Python Virtual Environment

## What is a Virtual Environment?

A Python virtual environment is an isolated environment that allows you to install packages and dependencies specific to a project without affecting the global Python installation. This ensures that projects are independent and helps prevent version conflicts between packages.

## Setting Up a Virtual Environment

### 1. Ensure Python is Installed

Make sure you have Python 3.7 or higher installed on your system. You can check your Python version by running:

```bash
python --version
```

or

```bash
python3 --version
```

### 2. Create a Virtual Environment

Navigate to your project directory:

```bash
cd path/to/movie_recommender_system
```

Create a virtual environment named `venv`:

#### On Windows:

```bash
python -m venv venv
```

#### On macOS and Linux:

```bash
python3 -m venv venv
```

This will create a new directory called `venv` in your project folder, containing the virtual environment.

### 3. Activate the Virtual Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS and Linux:

```bash
source venv/bin/activate
```

After activation, your command prompt or terminal will typically show the name of the virtual environment, indicating that it's active.

### 4. Install Required Packages

With the virtual environment activated, install the project's dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, you can install packages individually:

```bash
pip install Flask Werkzeug pandas
```

### 5. Deactivate the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

## Benefits of Using a Virtual Environment

- **Isolation**: Keeps project dependencies separate.
- **Consistency**: Ensures that the project runs with the same package versions, avoiding compatibility issues.
- **Manage Multiple Projects**: Allows you to work on multiple projects with different dependencies simultaneously.

## Additional Tips

- **Reproducing Environments**: If you share your project, others can recreate the same environment by creating a virtual environment and installing packages from `requirements.txt`.
- **Updating `requirements.txt`**: If you install new packages, update `requirements.txt`:

  ```bash
  pip freeze > requirements.txt
  ```

- **Checking Active Environment**: To verify that the virtual environment is active, run:

  ```bash
  which python    # macOS/Linux
  where python    # Windows
  ```

  The path should point to the `venv` directory.

---