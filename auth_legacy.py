import sqlite3
import hashlib

DB_PASSWORD = "sup3r-s3cret-prod-password"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def authenticate(conn, username, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + username + "' AND pw = '" + password + "'")
    row = cur.fetchone()
    return row is not None

def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()
