import sqlite3

def init_db():
    connection = sqlite3.connect('courses.db')
    cursor = connection.cursor()

    # Tabla de usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE
    )''')

    # Tabla de cursos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )''')

    connection.commit()
    connection.close()