import os
import secrets
from PIL import Image
from flask import get_flashed_messages, render_template, url_for, redirect, flash, redirect, request, abort
from commerceapp import app, db, bcrypt
from commerceapp.forms import RegistrationForm, LoginForm, DashboardForm, FoodForm, TablesForm, EditUserForm
from commerceapp.models import User, Order, Tables
from flask_login import login_user, current_user, logout_user, login_required


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
        flash("Food booked successfully", 'success')
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
        flash("Table successfully booked", 'success')
        return redirect(url_for('tables'))
    # else:
    #     flash("Try again", 'danger')
    #     return redirect(url_for('tables'))
    return render_template('tables.html', form=form)


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


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = DashboardForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash("Account updated successfully", 'success')
            return redirect('dashboard')
    image_file = url_for('static', filename="img/" + current_user.image_file)
    return render_template('dashboard.html', form=form, image_file=image_file)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        if form.validate() == True:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash("Registration successfull", 'success')
            return render_template('home.html')
            # flash('All fields are required.')
            # return render_template('register.html', form=form)
        else:
            return render_template('register.html', form=form)
            # flash("Registration successfull", 'success')
            # return render_template('index.html')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # if form.email.data == "enugu@gmail.com" and form.password.data == "1234567890":
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("login successful", 'success')
            return redirect(url_for('home'))
        else:
            flash("email not correct")
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/admin')
def admin():
    users = User.query.all()
    food = Order.query.all()
    table = Tables.query.all()
    if current_user.id != 2:
        flash('your mad! u cant access this page', 'danger')
        return redirect(url_for('home', users=users, food=food, table=table))
    else:
        render_template('Admin/index.html', users=users, food=food, table=table)

    return render_template('Admin/index.html', users=users, food=food, table=table)


@app.route("/edit_user/<int:user_id>", methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    if current_user.id != 2:
        abort(403)
    form = EditUserForm()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        db.session.commit()
        flash("User updated successfully", 'success')
        return redirect(url_for("admin"))
        # return render_template('Admin/index.html', form=form)
    elif request.method == 'Get':
        form.username.data = user.username
        form.email.data = user.email
    return render_template('Admin/editUser.html', form=form)


@app.route("/delete_user/<int:user_id>", methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if current_user.id != 2:
        abort(403)
    db.session.delete(user)
    db.session.commit()
    flash("deleted", 'success')
    return redirect(url_for('admin'))
    return render_template("Admin/index.html", user=user)


@app.route("/delete_food/<int:food_id>", methods=['GET', 'POST'])
def delete_food(food_id):
    food = Order.query.get_or_404(food_id)
    if current_user.id != 2:
        abort(403)
    db.session.delete(food)
    db.session.commit()
    flash("deleted", 'success')
    return redirect(url_for('admin'))
    return render_template("Admin/index.html", food=food)


@app.route("/delete_table/<int:table_id>", methods=['GET', 'POST'])
def delete_table(table_id):
    tables = Tables.query.get_or_404(table_id)
    if current_user.id != 2:
        abort(403)
    db.session.delete(tables)
    db.session.commit()
    flash("deleted", 'success')
    return redirect(url_for('admin'))
    return render_template("Admin/index.html", tables=tables)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
