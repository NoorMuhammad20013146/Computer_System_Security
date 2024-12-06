# Secure function: Using prepared statements
def login_secure(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"Executing secure query: {query} with parameters ({username}, {password})")
    cursor.execute(query, (username, password))
    return cursor.fetchall()

print("\nSecuring Against SQL Injection...")
secure_result = login_secure(malicious_username, malicious_password)
if secure_result:
    print("Vulnerability still exists (not expected).")
else:
    print("SQL Injection Mitigated Successfully!")