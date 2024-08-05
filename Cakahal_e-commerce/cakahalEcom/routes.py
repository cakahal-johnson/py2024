import os
import secrets
from PIL import Image
from flask import get_flashed_messages, render_template, url_for, flash, redirect, request, current_app
from cakahalEcom import app, db, bcrypt
from cakahalEcom.forms import RegistrationForm, LoginForm, UpdateDashboardForm, FoodForm, TablesForm, PostForm
from cakahalEcom.models import User, Order, Tables, Post
from flask_login import login_user, current_user, logout_user, login_required, fresh_login_required


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/food', methods=['GET', 'POST'])
def food():
    form = FoodForm()
    if form.validate_on_submit():
        order = Order(Foodname=form.Foodname.data, Foodtype=form.Foodtype.data, FoodQuantity=form.FoodQuantity.data,
                      Delivery_Time=form.Delivery_Time.data, Address=form.Address.data, author=current_user)
        db.session.add(order)
        db.session.commit()
        flash('Food booked successfully', 'success')
        return redirect(url_for('food'))
    return render_template('food.html', form=form)


@app.route('/tables', methods=['GET', 'POST'])
def tables():
    form = TablesForm()
    if form.validate_on_submit():
        book = Tables(Day=form.Day.data, Hour=form.Hour.data, Fullname=form.Fullname.data,
                      No_persons=form.No_persons.data, Phone=form.Phone.data, author=current_user)
        db.session.add(book)
        db.session.commit()
        flash('Table successfully booked', 'success')
        return redirect(url_for('tables'))
    # else:
    #     flash("Try again", 'danger')
    #     return redirect(url_for('tables'))
    return render_template('tables.html', form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_fn)
    form_picture.save(picture_path)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = UpdateDashboardForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash(f'Update successfully for {form.username.data}!', 'success')
            return redirect(url_for('dashboard'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.picture.data = current_user.image_file
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('dashboard.html', form=form, image_file=image_file)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Registration successfully for {form.username.data}!', 'success')
            return redirect(url_for('home'))
            # return render_template('home.html')
            # flash('All fields are required.')
            # return render_template('register.html', form=form)
        else:
            return render_template('register.html', form=form)
            # flash("Registration successfull", 'success')
            # return render_template('home.html')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # if form.email.data == "enugu@gmail.com" and form.password.data == "1234567890":
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Login successful with {form.email.data}', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login Unsuccessful, Please Sign Up", 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/admin')
def admin():
    users = User.query.all()
    food = Order.query.all()
    table = Tables.query.all()
    if current_user.id != 1:
        flash('Oops it only admin, u cant access this page', 'danger')
        return redirect(url_for('home', users=users, food=food, table=table))
    else:
        render_template('Admin/AdminHome.html', users=users, food=food, table=table)

    return render_template('Admin/AdminHome.html', users=users, food=food, table=table)


@app.route('/myfood')
def myfood():
    posts = Post.query.all()
    return render_template('myfood.html', posts=posts)


def blog_image(photo):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.split(photo.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/assets/image', picture_fn)
    photo.save(picture_path)

    return picture_fn


@app.route('/food_blog', methods=['GET', 'POST'])
@login_required
def food_blog():
    global image_file
    form = PostForm()
    if form.validate_on_submit():
        if form.image_1.data:
                image_file = blog_image(form.image_1.data)
                image_pic = image_file
        title = form.title.data
        content = form.content.data
        author = current_user
        post = Post(title=title, content=content, image_pic=image_pic, author=author)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('myfood'))
    return render_template('Admin/foodblog.html', form=form)


# @app.route("/post/<int:post_id>")
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template('Admin/myfood.html',  posts=posts)



@app.route("/logout")
def logout():
    logout_user()
    # session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('home'))
