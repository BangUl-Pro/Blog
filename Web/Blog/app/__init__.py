from flask import Flask


app = Flask(__name__)
app.secret_key = 'blog'


from app.routes import index, user
