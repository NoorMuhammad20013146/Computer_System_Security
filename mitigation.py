# Secure function: Using prepared statements
def login_secure(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"Executing secure query: {query} with parameters ({username}, {password})")
    cursor.execute(query, (username, password))