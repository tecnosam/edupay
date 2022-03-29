import sqlalchemy
from app import flask_app, db
from flask import render_template, session, redirect, url_for, flash

from app.models.order_models import Order
from app.models.service_models import Service
from app.models.status_models import Status

from app.resources.order_resource import validate_payment


@flask_app.route('/orders', methods=['GET', 'POST'])
def orders():

    if 'student_data' not in session and 'staff_data' not in session:
        return redirect('/')

    services = Service.query.all()

    if 'student_data' in session:

        student = session['student_data']
        orders = Order.query.filter_by(student_id=student['id'])

    elif 'staff_data' in session:
        orders = Order.query.all()

    status_modes = Status.query.all()

    return render_template('pages/orders.html',
        services=services, orders=orders, status_modes=status_modes)

@flask_app.route("/services/<service_id>/place-order/<reference>")
def place_order(service_id, reference):

    if 'student_data' not in session:
        return redirect('/')

    student_id = session['student_data']['id']

    if validate_payment(reference, service_id):

        try:

            Order.add(service_id, student_id, reference)

            flash("Payment Successful")

        except sqlalchemy.exc.IntegrityError:

            db.session.rollback()
            flash("This receipt is already registered with another order")

    else:
        # it did not pass the default checks
        flash("Your Payment is Invalid")

    return redirect(url_for('orders'))
