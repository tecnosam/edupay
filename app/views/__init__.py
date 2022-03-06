import sqlalchemy
from app import flask_app, db
from flask import render_template, session, redirect, url_for, request
from app.models.order_models import Order
from app.models.product_models import Product

from app.views.auth_views import *
from app.resources.order_resource import validate_payment

@flask_app.route('/')
def index():
    if 'student_data' in session:
        return redirect(url_for('orders'))
    
    return redirect(url_for('student_login'))

@flask_app.route('/orders', methods=['GET', 'POST'])
def orders():
    if 'student_data' not in session:
        return redirect('/')

    student = session['student_data']

    products = Product.query.all()
    orders = Order.query.filter_by(student_id=student['id'])

    return render_template('pages/orders.html', products=products, orders=orders)

@flask_app.route("/products/<product_id>/place-order/<reference>")
def place_order(product_id, reference):

    if 'student_data' not in session:
        return redirect('/')

    student_id = session['student_data']['id']

    if validate_payment(reference, product_id):

        try:

            Order.add(product_id, student_id, reference)

            flash("Payment Successful")

        except sqlalchemy.exc.IntegrityError:

            db.session.rollback()
            flash("This receipt is already registered with another order")

    else:
        # it did not pass the default checks
        flash("Your Payment is Invalid")
    
    return redirect(url_for('orders'))
