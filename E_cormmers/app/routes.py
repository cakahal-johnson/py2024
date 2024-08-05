import os
import secrets
from django.core import mail
from flask_mail import Mail, Message
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, current_app
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, FoodForm, TablesForm, BlogForm, MenuForm, \
    ImageForm
from app.models import User, Order, Tables, Post, Menu, ImageBlog
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/menu", methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')


@app.route("/blog", methods=['GET', 'POST'])
def blog():
    posts = Post.query.all()
    form = BlogForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            img_file = picture_file
        title = form.title.data
        content = form.content.data
        author = current_user
        picture = form.picture.data
        posts = Post(title=title, content=content, picture=picture, author=author, img_file=img_file)
        db.session.add(posts)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('blog'))
    return render_template('blog.html', post=posts, form=form)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


#
# @app.route("/foods", methods=['GET', 'POST'])
# @login_required
# def foods():
#     posts = Post.query.all()
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(foods_name=form.foods_name.data, foods_type=form.foods_type.data, foods_price=form.foods_price.data,
#                     delivery_time=form.delivery_time.data, location=form.location.data, author=current_user)
#         db.session.add(post)
#         db.session.commit()
#         flash('Successfully Send', 'success')
#         return redirect(url_for('foods'))
#     return render_template('food.html', form=form, posts=posts)
#

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        msg = Message('Hello', sender='christabelkaryn@gmail.com', recipients=['user.email'])
        msg.body = "Hello Flask message sent from Flask-Mail"
        mail.send(msg)
        flash('Your account has been Created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have logged in successfully.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('login unsuccessful.please check your Email and password', 'danger')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('home'))


#
# @app.route('/logout/<int:post_id>/logout')
# @login_required
# def logout(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Your post has been deleted!', 'success')
#     logout_user()
#     return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', image_file=image_file, form=form)


@app.route('/food', methods=['GET', 'POST'])
@login_required
def food():
    form = FoodForm()
    if form.validate_on_submit():
        order = Order(Foodname=form.Foodname.data, Foodtype=form.Foodtype.data, FoodQuantity=form.FoodQuantity.data,
                      Delivery_Time=form.Delivery_Time.data, Address=form.Address.data, author=current_user)
        db.session.add(order)
        db.session.commit()
        flash("Food booked successfully", 'success')
        return redirect(url_for('food'))
    return render_template('food.html', form=form)


@app.route('/tables', methods=['GET', 'POST'])
@login_required
def tables():
    form = TablesForm()
    if form.validate_on_submit():
        book = Tables(Day=form.Day.data, Hour=form.Hour.data, Fullname=form.Fullname.data,
                      No_persons=form.No_persons.data, Phone=form.Phone.data, author=current_user)
        db.session.add(book)
        db.session.commit()
        flash("Table successfully booked", 'success')
        return redirect(url_for('tables'))
    return render_template('tables.html', form=form)


@app.route('/admin')
def admin():
    users = User.query.all()
    food = Order.query.all()
    table = Tables.query.all()
    if current_user.id != 2:
        flash('your mad! u cant access this page', 'danger')
        return redirect(url_for('home', users=users, food=food, table=table))
    else:
        render_template('Admin/home.html', users=users, food=food, table=table)

    return render_template('Admin/home.html', users=users, food=food, table=table)


@app.route("/delete_food/<int:foods_id>", methods=['GET', 'POST'])
def delete_food(foods_id):
    foods = Order.query.get_or_404(foods_id)
    if current_user.id != 2:
        abort(403)
    db.session.delete(foods)
    db.session.commit()
    flash("deleted", 'success')
    return redirect(url_for('admin'))
    return render_template("Admin/home.html", foods=foods)


@app.route("/delete_table/<int:tables_id>", methods=['GET', 'POST'])
def delete_table(tables_id):
    tables = Tables.query.get_or_404(tables_id)
    if current_user.id != 2:
        abort(403)
    db.session.delete(tables)
    db.session.commit()
    flash("deleted", 'success')
    return redirect(url_for('admin'))
    return render_template("Admin/home.html", table=table)


@app.route('/')
def upload_form():
    return render_template('upload.html')


# @app.route('/', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         # print('upload_image filename: ' + filename)
#         flash('Image successfully uploaded and displayed below')
#         return render_template('upload.html', filename=filename)
#     else:
#         flash('Allowed image types are -> png, jpg, jpeg, gif')
#         return redirect(request.url)


# @app.route('/display/<filename>')
# def display_image(filename):
#     # print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route("/main_menu", methods=['GET', 'POST'])
def main_menu(title=None, content=None, category=None, price=None):
    global image_file
    # posts = Post.query.all()
    form = BlogForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = blog_image(form.image.data)
            image_file = picture_file
        category = form.category.data
        price = form.price.data
        title = form.title.data
        content = form.content.data
        author = current_user
        post = Post(category=category, price=price, title=title, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        title = title
        content = content
        category = category
        price = price,
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('Admin/main_menu.html', image_file=image_file, form=form, title=title, category=category,
                           price=price, content=content)


@app.route("/main_blog", methods=['GET', 'POST'])
def main_blog(title=None, content=None):
    global image_file
    # posts = Post.query.all()
    form = MenuForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = blog_image(form.image.data)
            image_file = picture_file
        title = form.title.data
        content = form.content.data
        author = current_user
        post = Post(title=title, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        title = title
        content = content
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('Admin/main_blog.html', image_file=image_file, form=form, title=title, content=content)


def blog_image(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.split(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


@app.route('/food_img', methods=['GET', 'POST'])
def food_img():
    form = ImageForm()
    if request.method == 'True':
        if form.validate_on_submit():
            image_1 = save_picture(form.image_1.data)
            image_2 = save_picture(form.image_2.data)
            image_3 = save_picture(form.image_3.data)
            image_4 = save_picture(form.image_4.data)
            author = current_user
            post = ImageBlog(image_1=image_1, image_2=image_2, image_3=image_3, image_4=image_4,  author=author)
            db.session.add(post)
            db.session.commit()
            flash('upload is successful', 'success')
            return redirect(url_for('home'))
        else:
            flash("fill in the form", 'danger')
            return redirect(url_for('Admin/food_img'))
    return render_template('Admin/food_img.html', form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.split(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn
