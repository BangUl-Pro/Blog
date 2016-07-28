from app import app
from app.managers.url_manager import LOGIN_URL
from flask import render_template


@app.route(LOGIN_URL)
def login():
    render_template('login.html')
