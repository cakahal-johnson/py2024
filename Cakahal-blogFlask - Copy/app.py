import os
from forms import PostForm
from datetime import datetime
from flask import Flask, render_template, abort, session, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
import sqlalchemy
from flask_mail import Mail, Message
from config import mail_username, mail_password

PEOPLE_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/flask_blog"
app.config['SECRET_KEY'] = "mysecretkeyismysecretkey"
app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)
db = SQLAlchemy(app)
admin = Admin(app, template_mode='bootstrap4')


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    subtitle = db.Column(db.String(255))
    content = db.Column(db.Text)
    author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_file = db.Column(db.String(150), nullable=False, default='post-sample-image.jpg')
    slug = db.Column(db.String(255))


class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)


class NotificationsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/notify.html')


class UploadView(BaseView):
    @expose('/')
    def index(self):
        form = PostForm()
        return self.render('admin/upload.html', form=form)


admin.add_view(SecureModelView(Posts, db.session))
admin.add_view(NotificationsView(name='Notifications', endpoint='notify'))
admin.add_view(UploadView(name='Upload', endpoint='upload'))


@app.route("/")
def home():
    posts = Posts.query.all()
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<string:slug>")
def post(slug):
    try:
        post = Posts.query.filter_by(slug=slug).one()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
        return render_template("post.html", post=post, image_file=full_filename)
    except sqlalchemy.exc.NoResultFound:
        abort(404)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        msg = Message(subject=f"Mail from {name}", body=f"Name: {name}\nE-mail: {email}\nPhone: {phone}\n\n\n{message}",
                      sender=mail_username, recipients=['cakahaljohnson@outlook.com'])
        mail.send(msg)
        return render_template("contact.html", success=True)
    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("email") == "testing@gmail.com" and request.form.get("pass") == "12345":
            session['logged_in'] = True
            return redirect("/admin")
        else:
            return render_template("login.html", failed=True)
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=7070)
