from flask import Flask, render_template, request, session, url_for, redirect
from flask.globals import request
from functions import Bank

app = Flask(__name__)
users = {}
print(users)
app.secret_key = 'hghdhudyuds78783e7$$%%'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username

            user = Bank(session['user'])

            print(user.show_details())

            print('Login successfully')
            return render_template('index.html')
        else:
            print("Username dosen't exits!")
            return render_template('login.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            print('User already exists')
            return render_template('register.html')
        else:
            password = request.form['password']
            users[username] = password
            print('user created')
            print(users)
            return render_template('index.html')
    else:
        return render_template('register.html')


@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == "POST":
        amount = request.form['deposit']
        user.deposit(amount)
        print(user.show_details())
        return render_template('deposit.html')
    else:
        return render_template('deposit.html')


@app.route('/withdraw')
def withdraw():
    if request.method == "POST":
        amount = request.form['withdraw']
        user.withdraw(amount)
        print(user.show_details())
        return render_template('withdraw.html')
    else:
        return render_template('withdraw.html')


if __name__ == "__main__":
    app.run(debug=True, port=1010)
