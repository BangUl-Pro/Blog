from flask import render_template
from app import app
from app.managers.url_manager import LOGIN_URL
from app.routes import user
from app.managers import db_manager


@app.route('/')
def root():
    return render_template('index.html',
                           login_url=LOGIN_URL)
