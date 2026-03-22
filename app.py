from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "dan-secret"

# ዳታቤዝ መፍጠር
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (phone TEXT PRIMARY KEY, username TEXT, password TEXT, balance REAL DEFAULT 0.0)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    if 'user' in session:
        return render_template('index.html', balance=session['balance'])
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE phone=? AND password=?", (phone, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user'] = user[0]
            session['balance'] = user[3]
            return redirect('/')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        phone = request.form['phone']
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (phone, username, password) VALUES (?, ?, ?)", (phone, username, password))
            conn.commit()
        except:
            return "ይህ ስልክ ቁጥር ተመዝግቧል!"
        conn.close()
        return redirect('/login')
    return render_template('register.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
  
