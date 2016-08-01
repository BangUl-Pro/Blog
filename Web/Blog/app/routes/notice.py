from app import app
from app.managers.url_manager import WRITE_NOTICE_URL
from flask import redirect, url_for, render_template, request, session
from app.forms.notice import NoticeForm
from app.models.notice import Notice


@app.route(WRITE_NOTICE_URL, methods=['GET', 'POST'])
def write_notice():
    form = NoticeForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        category = form.category.data
        print('category = {}'.format(category))
        user = session.get('user')
        print('user = {}'.format(user.id))
        notice = Notice(title, content, user.id, category)
        notice.insert_notice()
        return redirect(url_for('root'))
    return render_template('write_notice.html', form=form)
