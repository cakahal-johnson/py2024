from datetime import datetime
from cakahalEcom import db
from cakahalEcom import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(60), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    order = db.relationship('Order', backref='author', lazy=True)
    table = db.relationship('Tables', backref='author', lazy=True)
    post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Foodname = db.Column(db.Text, nullable=False)
    Foodtype = db.Column(db.Text, nullable=False)
    FoodQuantity = db.Column(db.Text, nullable=False)
    date_orderd = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    Address = db.Column(db.String(120), unique=True, nullable=False)
    Delivery_Time = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Order('{self.Foodname}','{self.FoodQuantity}','{self.Foodtype}','{self.Address}','{self.Delivery_Time}')"


class Tables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Day = db.Column(db.Text, nullable=False)
    Hour = db.Column(db.String(120), nullable=False)
    Fullname = db.Column(db.String(20), unique=True, nullable=False)
    date_orderd = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    No_persons = db.Column(db.String(120), nullable=False)
    Phone = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return f"Tables('{self.Day}','{self.Hour}','{self.Fullname}','{self.No_persons}','{self.Phone}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(60), nullable=False, default='default.png')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.image_file}', '{self.content}')"
