import sqlite3

# Simulate a database connection
conn = sqlite3.connect(':memory:')  # In-memory database for demonstration
cursor = conn.cursor()

# Create a sample users table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
''')