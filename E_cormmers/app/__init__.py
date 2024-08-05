from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
# from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
# from flask_uploads import UploadSet, configure_uploads, IMAGES, DATA, ALL
import os
# from app.routes import UPLOAD_FOLDER

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = '493d18cba56d77f3b1a10af73e21af17'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E_commerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTO_DEST'] = os.path.join(basedir, 'static/img')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'christabelkaryn@gmail.com@gmail.com'
app.config['MAIL_PASSWORD'] = '789775789971'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

from app import routes
