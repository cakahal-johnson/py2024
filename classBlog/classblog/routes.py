from flask import render_template, session, request, redirect, url_for, flash
from classblog import app
from classblog.forms import RegistrationForm, LoginForm
from classblog.models import User, Post


@app.route("/")
def home():
    return render_template('index.html', title='Home|Blog')


@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register|Blog', form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123456':
            flash(f'Welcome {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title='Login|Blog', form=form)
