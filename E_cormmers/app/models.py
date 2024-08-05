from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg.png')
    order = db.relationship('Order', backref='author', lazy=True)
    password = db.Column(db.String(60), nullable=False, )
    table = db.relationship('Tables', backref='author', lazy=True)
    post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Foodname = db.Column(db.Text, nullable=False)
    Foodtype = db.Column(db.Text, nullable=False)
    FoodQuantity = db.Column(db.Text, nullable=False)
    date_orderd = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    Address = db.Column(db.Text, unique=False, nullable=False)
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
    Phone = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f"Tables('{self.Day}','{self.Hour}','{self.Fullname}','{self.No_persons}','{self.Phone}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg.png')
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.content}', '{self.image_file}')"


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_title = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    price = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.sub_title}', '{self.price}', '{self.title}', '{self.content}', '{self.image_file}')"


class ImageBlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_1 = db.Column(db.String(60), nullable=False, default='image.jpg')
    image_2 = db.Column(db.String(60), nullable=False, default='image.jpg')
    image_3 = db.Column(db.String(60), nullable=False, default='image.jpg')
    image_4 = db.Column(db.String(60), nullable=False, default='image.jpg')

    def __repr__(self):
        return f"ImageBlog('{self.image_1}',{self.image_2},'{self.image_3}','{self.image_4}')"
