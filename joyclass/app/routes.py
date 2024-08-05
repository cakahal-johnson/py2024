from flask import render_template, url_for, flash, redirect, request






@app.route("/")
def index():
    return render_template('index.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/menu")
def menu():
    return render_template('menu.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if not form.validate() == True:
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Registration successfull", 'success')
            return redirect('/')
            # flash('All fields are required.')
            # return render_template('register.html', form=form)
        else:
            return render_template('register.html', form=form)
            # flash("Registration successfull", 'success')
            # return render_template('home.html')

    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate() == True:
            # if form.email.data() == 'test@gmail.com' and form.password.data() == 'testing':
            flash('You have been logged in!', 'success')
            return render_template('index.html')
        else:
            flash('Login Unsuccessful Please check username and password', 'danger')
            return redirect(url_for('register'))
    return render_template('login.html', form=form)