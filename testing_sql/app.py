from flask import Flask, redirect, url_for, render_template, request, session, flash, current_app, app
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy



def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config")
    db = SQLAlchemy(app)

    # import project.models
    from models import user

    with app.app_context():
        db.create_all()

    app.secret_key = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.permanent_session_lifetime = timedelta(days=1)

    def test_user_model(app):

        with app.app_context():
            db.session.add(user)
            db.session.commit()

    return app


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        users = request.form["nm"]
        session["user"] = users
        flash("Login successful.", "info")

        return redirect(url_for("user"))
    else:

        if "user" in session:
            flash("Already logged in.")
            return redirect((url_for("user")))
        return render_template("login.html")


@app.route('/user', methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("Not logged in.")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect((url_for("login")))


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True, port=9902)
