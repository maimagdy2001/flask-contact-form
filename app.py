from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Secret key for form CSRF protection

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database (create table if not exists)
def init_db():
    conn = get_db_connection()
    conn.execute("drop TABLE users")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT ,last_name TEXT,email TEXT,phone_number INTEGER,reason TEXT)")
    #with app.open_resource('schema.sql', mode='r') as f:
    # conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

init_db()  # Initialize the database when the app starts

# Route to display the form
@app.route('/')
def contact():
    return render_template('contact.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        reason = request.form['reason']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (first_name, last_name, phone_number, email, reason) VALUES (?, ?, ?, ?, ?)',
                    (first_name, last_name, phone_number, email, reason))
        conn.commit()
        conn.close()
        
        return redirect(url_for('contact'))
@app.route('/contacts')
def contacts():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    contacts = cursor.fetchall()
    return render_template('contacts_list.html', contacts=contacts)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

