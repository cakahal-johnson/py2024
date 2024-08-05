from sys import path
from flask_login import UserMixin

from tech import db
from datetime import datetime


class Addpackage(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False, unique=False)
    price = db.Column(db.Numeric(10,2), nullable=False, unique=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False, unique=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    invest = db.relationship('Invest', backref=db.backref('invests', lazy=True))

    loan = db.relationship('Loan', backref=db.backref('posts', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image.jpg')

    def __repr__(self):
        return '<Addpackage %r>' % self.name


#brand product
class Invest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False, unique=False)
    invest_id = db.Column(db.Integer, db.ForeignKey('invest.id'), nullable=False)

    def __repr__(self):
        return '<Invest %r>' % self.name


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False, unique=False)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'), nullable=False)

    def __repr__(self):
        return '<Loan %r>' % self.name


db.create_all()

# def create_database(app):
#     if not path.exists("tech/" + "project.db"):
#         db.create_all(app=app)
#         print("database created ")


