from flask import render_template
from app import app
from app.managers.url_manager import LOGIN_URL


@app.route('/')
def route():
    return render_template('index.html',
                           login_url=LOGIN_URL)
