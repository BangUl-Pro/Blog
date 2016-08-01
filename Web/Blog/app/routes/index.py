from flask import render_template, session


from app import app
from app.managers.url_manager import LOGIN_URL, SIGN_UP_URL, LOGOUT_URL, WRITE_NOTICE_URL


@app.route('/')
def root():
    user = session.get('user')
    return render_template('index.html',
                           login_url=LOGIN_URL,
                           sign_up_url=SIGN_UP_URL,
                           user=user,
                           logout_url=LOGOUT_URL,
                           write_notice_url=WRITE_NOTICE_URL)
