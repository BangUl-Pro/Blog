from flask import Flask
from flask_redis import FlaskRedis

redis_store = FlaskRedis()
app = Flask(__name__)
redis_store.init_app(app)


from app.routes import index, user
