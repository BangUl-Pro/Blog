from app import app
from app.managers.url_manager import SETTING_URL, UPDATE_PROFILE_URL
from app.forms.user import SignUpForm
from flask import request, render_template, session


@app.route(SETTING_URL)
def setting():
    form = SignUpForm(request.form)
    user = session.get('user')
    print(user)
    return render_template('setting.html',
                           form=form,
                           user=user,
                           update_profile_url=UPDATE_PROFILE_URL)
