from flask import Flask


app = Flask(__name__)
app.secret_key = 'secret'


from app.routes import index
