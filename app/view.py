
from app import app
from flask import render_template, url_for, request, redirect

# Página Inicial
@app.route  ('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')

# Página de Login
@app.route ('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')