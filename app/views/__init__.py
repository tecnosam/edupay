from app import flask_app
from flask import render_template, session, redirect, url_for
from app.models.product_models import Product

from app.views.auth_views import *

@flask_app.route('/')
def index():
    if 'student_data' in session:
        return redirect(url_for('orders'))
    
    return redirect(url_for('student_login'))

@flask_app.route('/orders')
def orders():
    products = Product.query.all()
    return render_template('pages/orders.html', products=products)
