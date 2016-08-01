from flask import render_template, session
from app import app
from app.managers.url_manager import LOGIN_URL, SIGN_UP_URL, LOGOUT_URL, WRITE_NOTICE_URL
from app.models.notice import get_notices, get_latest_notices


@app.route('/')
def root():
    user = session.get('user')
    print('notices = {}'.format(get_latest_notices()))
    return render_template('index.html',
                           login_url=LOGIN_URL,
                           sign_up_url=SIGN_UP_URL,
                           user=user,
                           logout_url=LOGOUT_URL,
                           write_notice_url=WRITE_NOTICE_URL,
                           notices=get_notices(),
                           latest_notices=get_latest_notices())
