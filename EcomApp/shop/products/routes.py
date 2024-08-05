from flask import render_template, session, request, redirect, url_for, flash
from .models import Brand, Category

from shop import app, db


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to you database', 'success')
        
    return render_template('products/addbrand.html')
