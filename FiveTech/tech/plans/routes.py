# from flask import redirect, render_template, url_for, flash, request
# from tech import db, app
# from .models import Invest, Loan
# from .forms import Addpackages
#
#
# @app.route('/addinvest', methods=['GET', 'POST'])
# def addinvest():
#     if request.method == "POST":
#         getinvest = request.form.get('invest')
#         invest = Invest(name=getinvest)
#         db.session.add(invest)
#         flash(f'Your Invest {getinvest} Package is Successfully please wait for confirmation in your dashboard!', 'success')
#         # db.session.commit()
#         return redirect(url_for('addinvest'))
#     return render_template('plans/addplan.html', invests='invests')
#
#
# @app.route('/addloan', methods=['GET', 'POST'])
# def addloan():
#     if request.method == "POST":
#         getinvest = request.form.get('loan')
#         loan = Loan(name=getinvest)
#         db.session.add(loan)
#         flash(f'Your Loan {getinvest} Package is Successfully please wait for confirmation in your dashboard!', 'success')
#         # db.session.commit()
#         return redirect(url_for('addloan'))
#     return render_template('plans/addplan.html')
#
#
# @app.route('/addpackage', methods=['POST', 'GET'])
# def addpackage():
#     invests = Invest.query.all()
#     loans = Loan.query.all()
#
#     form = Addpackages(request.form)
#     return render_template('plans/addpackage.html', invests=invests, loans=loans, title="Add Package page", form=form)