from flask import render_template, url_for, flash, redirect, request, session
from investment import app, db, bcrypt
from investment.forms import RegistrationForm, LoginForm
from investment.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("blog.html", title='Blog')


@app.route("/contact")
def contact():
    return render_template("/reachUs.html", title='Contact')


@app.route("/faq")
def faq():
    return render_template("/faq.html", title='Faq')


@app.route("/pricing")
def pricing():
    return render_template("/pricing.html", title='Pricing')


@app.route("/team")
def team():
    return render_template("/team.html", title='team')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        # if user.status == 'Admin':
        #     return redirect(url_for('backend'))
        else:
            flash('Login Unsuccessful. Please retry', 'danger')
    return render_template("/login.html", title='login', form=form)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(Firstname=form.Firstname.data, Lastname=form.Lastname.data, username=form.Firstname.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template("/signup.html", title='signup', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/admin")
@login_required
def admin():
    return render_template('admin/index.html', title='admin')


@app.route("/calendar")
@login_required
def calendar():
    return render_template('admin/calendar.html', title="calendar")


@app.route("/reachUs")
@login_required
def reachUs():
    return render_template('admin/reachUs.html', title="contact")


@app.route("/chat")
@login_required
def chat():
    return render_template('admin/chat.html', title="chat")


@app.route("/contact2")
@login_required
def contact2():
    return render_template('admin/contact2.html', title="contact2")


@app.route("/ticket")
@login_required
def ticket():
    return render_template('admin/ticket.html', title="ticket")


@app.route("/detail")
@login_required
def ContactDetail():
    return render_template('admin/detail.html', title="contact-detail")


@app.route("/email")
@login_required
def email():
    return render_template('admin/email.html', title="email")


@app.route("/emailDetail")
@login_required
def emailDetail():
    return render_template('admin/emailDetail.html', title="email-detail")


@app.route("/compose")
@login_required
def compose():
    return render_template('admin/compose.html', title="compose")


@app.route("/googleMap")
@login_required
def googleMap():
    return render_template('admin/map-google.html', title="googleMap")


@app.route("/widget2")
@login_required
def widget2():
    return render_template('admin/widget-2.html', title="widget-2")


@app.route("/widgetData")
@login_required
def widgetData():
    return render_template('admin/widget-data.html', title="widgetData")


@app.route("/widgetApps")
@login_required
def widgetApps():
    return render_template('admin/widget-apps.html', title="widgetApps")


@app.route("/widgetCharts")
@login_required
def widgetCharts():
    return render_template('admin/widget-charts.html', title="widgetCharts")

# HERE IS FOR THE BACKEND
@app.route("/backend")
def backend():
    return render_template("backend.html")