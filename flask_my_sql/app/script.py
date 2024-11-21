from flask import Flask, render_template, request
from app import app
from datetime import datetime
from mysql_python.db import insert_user, clear_table, read_table

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    print(f"Name: {name}, Email: {email}")
    insert_user(name, email)
    return '', 200

@app.route('/read')
def read():
    print(read_table())
    return 'read', 200

@app.route('/clear')
def clear():
    clear_table()
    return 'ok', 200