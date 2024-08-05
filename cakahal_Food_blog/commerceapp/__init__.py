from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


# from app import db

app = Flask(__name__)
app.secret_key = 'jjjjo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = "stmp.googlemail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'allenwalker.associate@gmail.com'
app.config['MAIL_PASSWORD'] = 'openmyaccaw'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

from commerceapp import routes
