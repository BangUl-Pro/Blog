from wtforms import StringField, PasswordField, Form
from wtforms.validators import InputRequired, Length, EqualTo, Email


class LoginForm(Form):
    id = StringField('ID', [
        InputRequired(message='아이디는 필수입니다.'),
        Length(min=6, message='%(min)d 글자 이상이여야 합니다.')
    ])

    password = PasswordField('Password', [
        InputRequired(message='비밀번호는 필수입니다.'),
        Length(min=6, message='%(min)d 글자 이상이여야 합니다.')
    ])


class SignUpForm(LoginForm):
    name = StringField('Name', [
        InputRequired(message='이름은 필수입니다.'),
    ])

    confirm = PasswordField('Confirm', [
        InputRequired(message='비밀번호 확인은 필수입니다.'),
        EqualTo('password', message='비밀번호와 일치해야합니다.')
    ])

    email = StringField('Email', [
        InputRequired(message='이메일은 필수입니다.'),
        Email(message='유효한 이메일을 입력하세요.')
    ])
