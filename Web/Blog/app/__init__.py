from flask import Flask
from flask_redis import FlaskRedis
from datetime import datetime
from app.managers.url_manager import NOTICE_DETAIL_URL


redis_store = FlaskRedis()
app = Flask(__name__)
redis_store.init_app(app)


def left_date_format_filter(time):
    cur_time = datetime.now()
    gap_time = int((cur_time - time).total_seconds())
    if gap_time > 86400:
        return str(time)[:10]
    elif gap_time > 3600:
        return '{} 시간 전'.format(int(gap_time / 3600))
    elif gap_time > 60:
        return '{} 분 전'.format(int(gap_time / 60))
    return '방금 전'

app.jinja_env.filters['left_date_format_filter'] = left_date_format_filter
app.jinja_env.globals['notice_detail_url'] = NOTICE_DETAIL_URL


from app.routes import index, user, notice, setting
