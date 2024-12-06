# Secure function: Using prepared statements
def login_secure(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"