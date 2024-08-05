from app import app
from flask import render_template, request, redirect, url_for, session


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


# @app.route("/contact/<name>") ********then in the html sections  = hello {{ name }} this name will return what is in the url
# def contact(name):
#     return render_template('contact.html', name=name) *********this is url binding whereby any name passed to url will display

#we want to create adding an article to a page,



@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/blog_form")
def blog_form():
    return render_template('blog_form.html')


# @app.route("/post")
# def post():
#     return render_template('post.html')


@app.route("/create-post", methods = ['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        return render_template('post.html', result=request.form)
    else:
        if 'username' in session and session['username'] == 'admin':
            return render_template('blog_form.html')
        else:
            return render_template('login.html')



@app.route('/login', methods = ['POST', 'GET'] )
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('/login'))

    return render_template('login.html')
