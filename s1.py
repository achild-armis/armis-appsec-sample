from flask import Flask, request, send_file
import sqlite3
import os


app = Flask(__name__)

# Vulnerable SQL injection endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # ⚠️
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    if user:
        return "Login successful!"
    else:
        return "Invalid credentials"

# Vulnerable directory traversal endpoint
@app.route('/get_file/<path:filename>')
def get_file(filename):
    file_path = os.path.join(app.root_path, 'files', filename)
    if not os.path.isfile(file_path):
        return "File not found", 404
    return send_file(file_path)

# Root route
@app.route('/')
def index():
    return "Welcome! Try `/login` or `/get_file/<filename>`"

if __name__ == '__main__':
    app.run(debug=True)
