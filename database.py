import sqlite3

def create_connection():
    conn = sqlite3.connect('nutritrack.db')
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
    
    # Create nutrition table
    cursor.execute('''CREATE TABLE IF NOT EXISTS nutrition (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        date TEXT NOT NULL,
                        calories INTEGER,
                        protein INTEGER,
                        fat INTEGER,
                        carbs INTEGER,
                        FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    # Create weight table
    cursor.execute('''CREATE TABLE IF NOT EXISTS weight (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        date TEXT NOT NULL,
                        weight REAL,
                        FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    conn.commit()

