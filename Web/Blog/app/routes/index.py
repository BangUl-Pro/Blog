from flask import render_template, session
from app import app
from app.managers.url_manager import LOGIN_URL, SIGN_UP_URL, LOGOUT_URL, WRITE_NOTICE_URL, SETTING_URL
from app.models.notice import get_notices, get_latest_notices
from app.models.category import get_categories


@app.route('/')
def root():
    user = session.get('user')
    return render_template('index.html',
                           login_url=LOGIN_URL,
                           sign_up_url=SIGN_UP_URL,
                           user=user,
                           logout_url=LOGOUT_URL,
                           setting_url=SETTING_URL,
                           write_notice_url=WRITE_NOTICE_URL,
                           notices=get_notices(),
                           categories=get_categories(),
                           latest_notices=get_latest_notices())
