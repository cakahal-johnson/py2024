from sys import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads
import os

# from tech.packages.models import create_database

basedir = os.path.abspath(os.path.dirname(__file__))
# create the extension
# db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = 'THISisMYsecretKEy'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)  # 16 megabytes
# configure_uploads(app, (photos, media )) # 32 megabytes

# patch_request_class(app)  # 16 megabytes
#  patch_request_class(app, 32 * 1024 * 1024)  # 32 megabytes


# initialize the app with the extension
db = SQLAlchemy(app)
db.init_app(app)
# create_database()
bcrypt = Bcrypt(app)


from tech.admin import routes
from tech.packages import routes


# def create_database(app):
#     if not path.exists("tech/" + "project.db"):
#         db.create_all(app=app)
#         print("database created ")


