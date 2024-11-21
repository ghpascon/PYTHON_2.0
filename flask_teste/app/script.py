from app import app
from flask import render_template,jsonify
from datetime import datetime

@app.route('/time')
def time():
    now = datetime.now().strftime('%H:%M:%S')
    return jsonify(time=now)