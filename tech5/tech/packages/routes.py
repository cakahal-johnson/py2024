from flask import redirect, render_template, url_for, flash, request, session, current_app
from tech import db, app, photos
from .models import Invest, Loan, Addpackage
from .forms import Addpackages
import secrets, os


@app.route('/addinvest', methods=['GET', 'POST'])
def addinvest():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
    if request.method == "POST":
        getinvest = request.form.get('invest')
        invest = Invest(name=getinvest)
        db.session.add(invest)
        flash(f'Your Invest {getinvest} Package is Successfully please wait for confirmation in your dashboard!', 'success')
        db.session.commit()
        return redirect(url_for('addinvest'))
    return render_template('plans/addplan.html', invests='invests')


@app.route('/addloan', methods=['GET', 'POST'])
def addloan():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
    if request.method == "POST":
        getinvest = request.form.get('loan')
        loan = Loan(name=getinvest)
        db.session.add(loan)
        flash(f'Your Loan {getinvest} Package is Successfully please wait for confirmation in your dashboard!', 'success')
        db.session.commit()
        return redirect(url_for('addloan'))
    return render_template('plans/addplan.html')


@app.route('/addpackage', methods=['POST', 'GET'])
def addpackage():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
    invests = Invest.query.all()
    loans = Loan.query.all()
    form = Addpackages(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        discount = form.stock.data
        stock = form.stock.data
        colors = form.color.data
        desc = form.description.data
        invest = request.form.get('invest')
        loan = request.form.get('loan')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        addpack = Addpackage(name=name, price=price, discount=discount, stock=stock, colors=colors, desc=desc, invest_id=invest, loan_id=loan, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpack)
        flash(f'The package {name} has been added to your database', 'success')
        db.session.commit()

        return redirect(url_for('admin'))
    return render_template('plans/addpackage.html', invests=invests, loans=loans, title="Add Package page", form=form)


# =====here we update packages ==============
@app.route('/updatepackage/<int:id>', methods=['GET', 'POST'])
def updatepackage(id):
    invests = Invest.query.all()
    loans = Loan.query.all()
    package = Addpackage.query.get_or_404(id)
    invest = request.form.get('invest')
    loan = request.form.get('loan')
    form = Addpackages(request.form)

    if request.method == 'POST':
        package.name = form.name.data
        package.price = form.price.data
        package.discount = form.discount.data
        package.invest_id = invest
        package.loan_id = loan
        package.colors = form.color.data
        package.desc = form.description.data
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + package.image_1))
                package.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                package.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")

        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + package.image_2))
                package.image_1 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                package.image_1 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")

        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + package.image_3))
                package.image_1 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                package.image_1 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        db.session.commit()
        flash(f'Your Package has been updated', 'success')
        return redirect('admin')

    form.name.data = package.name
    form.price.data = package.price
    form.discount.data = package.discount
    form.stock.data = package.stock
    form.color.data = package.colors
    form.description.data = package.desc

    return render_template('packages/updatepackage.html', invests=invests, loans=loans,  form=form)


# =====here we update invest=====
@app.route('/updateinvest/<int:id>', methods=['GET', 'POST'])
def updateinvest(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
    updateinvest = Invest.query.get_or_404(id)
    invest = request.form.get('invest')
    if request.method == "POST":
        updateinvest.name = invest
        flash(f'Your Invest has been Updated', 'success')
        db.session.commit()
        return redirect(url_for('invests'))
    return render_template('packages/updateinvest.html', title='Update Invest Page', updateinvest=updateinvest)


# =====here we update loan============
@app.route('/updateloan/<int:id>', methods=['GET', 'POST'])
def updateloan(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
    updateloan = Invest.query.get_or_404(id)
    loan = request.form.get('loan')
    if request.method == "POST":
        updateloan.name = loan
        flash(f'Your Invest has been Updated', 'success')
        db.session.commit()
        return redirect(url_for('loan'))
    return render_template('packages/updateinvest.html', title='Update Loan Page', loan=loan)