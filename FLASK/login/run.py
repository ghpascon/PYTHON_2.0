from flask import Flask,flash, render_template, request, redirect, url_for, session, jsonify
app = Flask(__name__)
app.secret_key = 'your_secret_key'
import json
from werkzeug.security import check_password_hash, generate_password_hash
from app import mysql_utils, route_functions

# Carregar configuração
with open('config/db.json') as db_file:
    db_config = json.load(db_file)

with open('config/master.json') as master_file:
    master_user = json.load(master_file)

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['senha']
        
        # Verificar usuário master
        if username == master_user['master_username'] and password == master_user['master_password']:
            session['user'] = master_user['master_name']
            session['username'] = master_user['master_username']
            return redirect(url_for('dashboard'))
        
        # Verificar usuário no banco de dados
        conn = mysql_utils.get_db_connection(db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        print(user)
        cursor.close()
        conn.close()

        print(generate_password_hash(password))

        if user and check_password_hash(user['password'], password):
            session['user'] = user['name']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        
        flash("Login falhou, verifique suas credenciais!")
        return render_template("login.html")
        

    return render_template('login.html')

# Rota protegida
@app.route('/')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

route_functions.functions(app)

if __name__ == '__main__':
    app.run(debug=True)

#pyinstaller --onefile --windowed --add-data "app;app" run.py
