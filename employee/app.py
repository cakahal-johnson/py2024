from flask import Flask, render_template, redirect, request, url_for, abort, flash
from models import db, Member


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SECRET_KEY'] = 'hgtatt@cakahal789A000@'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':

        hobby = request.form.getlist('hobbies')
        hobbies = ",".join(map(str, hobby))
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = hobbies
        country = request.form['country']

        members = Member(first_name=first_name, last_name=last_name, email=email, password=password,
                         gender=gender, hobbies=hobbies, country=country)

        db.session.add(members)
        db.session.commit()
        print(members)
        return redirect('/')


@app.route('/', methods=["GET", "POST"])
def RetrieveList():
    members = Member.query.all()
    return render_template('index.html', members=members)


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    members = Member.query.filter_by(id=id).first()

    if request.method =='POST':

        db.session.delete(members)
        db.session.commit()
        if members:
            hobby = request.form.getlist('hobbies')
            hobbies = ",".join(map(str, hobby))
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            gender = request.form['gender']
            hobbies = hobbies
            country = request.form['country']

            members = Member(first_name=first_name, last_name=last_name, email=email, password=password,
                             gender=gender, hobbies=hobbies, country=country)

            db.session.add(members)
            db.session.commit()
            return redirect('/')
            return f'Student with id = {id} Does not exist'

    return render_template('update.html', members=members)


@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    members = Member.query.filter_by(id=id).first()
    if request.method == 'POST':
        if members:
            db.session.delete(members)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True, port=9098)
