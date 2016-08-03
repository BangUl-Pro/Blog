from app import app
from app.managers.url_manager import SETTING_URL, UPDATE_PROFILE_URL, ADD_CATEGORY, REMOVE_CATEGORY, UPDATE_CATEGORY
from app.forms.user import SignUpForm
from flask import request, render_template, session
from app.models.category import get_categories


@app.route(SETTING_URL)
def setting():
    form = SignUpForm(request.form)
    user = session.get('user')
    return render_template('setting.html',
                           form=form,
                           user=user,
                           update_profile_url=UPDATE_PROFILE_URL,
                           categories=get_categories(),
                           add_category_url=ADD_CATEGORY,
                           remove_category_url=REMOVE_CATEGORY,
                           update_category_url=UPDATE_CATEGORY)
