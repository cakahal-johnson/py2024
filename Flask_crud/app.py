from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home Page')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')


@app.route('/addnewemployee')
def addnewemployee():
    return render_template('addnewemployee.html', title='Addnewemployee')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/singlemployeeprofile')
def singlemployeeprofile():
    return render_template('singlemployeeprofile.html', title='Singlemployeeprofile')


@app.route('/updateemployee')
def updateemployee():
    return render_template('updateemployee.html', title='Updateemployee')


@app.route('/frontpage')
def frontpage():
    return render_template('frontpage.html', title='cakahal')


@app.route('/tnc')
def tnc():
    return render_template('tnc.html', title='naka')


@app.route('/eportal')
def eportal():
    return render_template('bank/eportal.html', title='Eportal')


if __name__ == '__main__':
    app.run(debug=True, port=9091)