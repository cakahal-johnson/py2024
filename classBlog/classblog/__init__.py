from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] ='THISisMYsecretKEy'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ClassBlog.db"
db = SQLAlchemy(app)

from classblog import routes
