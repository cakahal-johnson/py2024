from flask import render_template, session, request, redirect, url_for, flash
from tech import app, bcrypt, db
from .forms import RegistrationForm, LoginForm
from .models import User
from tech.packages.models import Addpackage, Invest, Loan
import os


@app.route('/')
def home():
    return render_template("admin/home.html", title="Home")


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    packages = Addpackage.query.all()
    return render_template("admin/index.html", title="Admin Page", packages=packages)


@app.route('/invests')
def invests():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    invests = Invest.query.order_by(Invest.id.desc()).all()
    return render_template("admin/invest.html", title="Invest Page", invests=invests)


@app.route('/loan')
def loan():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    loans = Loan.query.order_by(Loan.id.desc()).all()
    return render_template("admin/invest.html", title="Invest Page", loans=loans)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'welcome {form.name.data} Thanks you for registering', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title='Registration page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} its nice to see you!', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash(f'Wrong Password please try again', 'danger')
    return render_template('admin/login.html', form=form, title='Login page')

