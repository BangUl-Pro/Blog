from app import app
from app.managers.url_manager import LOGIN_URL, SIGN_UP_URL
from flask import render_template, request, redirect, url_for
from app.forms.user import LoginForm, SignUpForm
from app.models.user import User


@app.route(LOGIN_URL, methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user_id = form.id.data
        password = form.password.data
        req_user = User(user_id, password)
        user = User.get_user(req_user)
        if user:
            return redirect(url_for('root'))
    return render_template('login.html', form=form)


@app.route(SIGN_UP_URL, methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        user_id = form.id.data
        password = form.password.data
        email = form.email.data
        user = User(user_id, password, name, email)
        res = User.insert_user(user)
        if res == 200:
            print('success')
            return redirect(url_for('root'))
        elif res == 301:
            # TODO 아이디 겹침
            print('아이디 겹침')
        elif res == 302:
            # TODO 이메일 겹침
            print('이메일 겹침')
    return render_template('sign_up.html', form=form)
