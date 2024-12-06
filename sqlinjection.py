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

# Insert some dummy data
cursor.executemany('INSERT INTO users (username, password) VALUES (?, ?)', [
    ('admin', 'admin123'),
    ('user1', 'password1'),
    ('user2', 'password2')
])
conn.commit()
