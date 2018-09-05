from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['MONGOALCHEMY_DATABASE'] = 'bookstore'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://<user_name>:<password>@ds143932.mlab.com:43932/bookstore'

db = MongoAlchemy(app)

from bookstore import routes