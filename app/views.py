from app import app
from flask import render_template


@app.route('/')
def Homepage():
    return render_template('index.html')