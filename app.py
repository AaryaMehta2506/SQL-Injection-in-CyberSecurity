from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="pass123",  # Your MySQL password
        database="vulnerable_db"
    )

@app.route('/')
def index():
    return '''
        <h2>Login</h2>
        <form action="/login" method="POST">
            Login ID: <input type="text" name="login_id"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
        <br>
        <a href="/register">Register Here</a>
    '''

@app.route('/register')
def register():
    return '''
        <h2>Register</h2>
        <form action="/register" method="POST">
            Login ID: <input type="text" name="login_id"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Register">
        </form>
    '''

@app.route('/register', methods=['POST'])
def register_user():
    login_id = request.form['login_id']
    password = request.form['password']

    # Secure query using parameterized statement
    query = "INSERT INTO users (login_id, password) VALUES (%s, %s)"

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, (login_id, password))  # Parameters are passed as a tuple
        conn.commit()
        return "Registration successful!"
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    login_id = request.form['login_id']
    password = request.form['password']

    # Secure query using parameterized statement
    query = "SELECT * FROM users WHERE login_id=%s AND password=%s"

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (login_id, password))  # Parameters are passed as a tuple
    user = cursor.fetchone()

    if user:
        return f"Welcome {user['login_id']}!"
    else:
        return "Login failed!"

if __name__ == '__main__':
    app.run(debug=True)
