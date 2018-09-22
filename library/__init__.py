from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='ec0fbc33bcfafdef4b52ad9f0ce75196'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from library import routes

