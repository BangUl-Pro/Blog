from app import app
from app.managers.url_manager import LOGIN_URL
from flask import render_template, request, redirect, url_for
from app.forms.user import LoginForm
from app.models.user import User


@app.route(LOGIN_URL, methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        id = form.id.data
        password = form.password.data
        user = User.get_user(id, password)
        if user:
            return redirect(url_for('root'))
    return render_template('login.html', form=form)
