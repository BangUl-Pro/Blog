from wtforms import Form, StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired


class NoticeForm(Form):
    title = StringField('Title', [
        InputRequired(message='제목은 필수입니다')
    ])

    content = TextAreaField('Content', [
        InputRequired(message='내용은 필수입니다')
    ])

    category = SelectField('Category', choices=[])
