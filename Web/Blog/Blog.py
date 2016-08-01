from app import app
from app.redis_session import RedisSessionInterface


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.session_interface = RedisSessionInterface()
    app.run(debug=True)

