from flask import render_template

from app import app
from app.managers.url_manager import LOGIN_URL, SIGN_UP_URL


@app.route('/')
def root():
    return render_template('index.html',
                           login_url=LOGIN_URL,
                           sign_up_url=SIGN_UP_URL)
