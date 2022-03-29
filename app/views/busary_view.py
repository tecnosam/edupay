from flask import render_template, redirect, request, url_for, session, flash
from app import flask_app

import sqlalchemy
from app.models.order_models import Order

from app.models.service_models import Service


@flask_app.route("/receipts")
def receipts():
    if 'staff_data' not in session:
        return redirect(url_for('staff_login'))

    return redirect(url_for('orders'))

@flask_app.route("/services", methods=['GET', 'POST'])
def services():

    if 'staff_data' not in session:
        return redirect(url_for('staff_login'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')

        method = request.form.get('_method', 'POST')

        try:

            if method.upper() =='PUT':
                service_id = request.form.get('id', 0)
                _service = Service.edit(service_id, name, price)

            else:
                _service = Service.add(name, price, session['staff_data']['id'])

            if _service is not None:
                flash("Successfully uploaded service/service")
            else:
                flash("There was an error locating this service")

        except sqlalchemy.exc.IntegrityError:
            print("oops")
            flash("A Service/Service with this name already exists")
    elif 'pop' in request.args:
        service_id = request.args['pop']
        _service = Service.delete(service_id)

        if _service is not None:
            flash("Successfully deleted service/service")
        else:
            flash("There was an error locating this service")


    services = Service.query.all()
    return render_template("pages/services.html", services=services)


@flask_app.route("/orders/<int:order_id>/change-status/<int:status_id>")
def change_order_status(order_id: int, status_id: int):
    if 'staff_data' not in session:
        redirect(url_for('staff_login'))

    order: Order = Order.change_status(order_id, status_id)

    if order is not None:
        flash("Successfully changed status")
    else:
        flash("Error locating order")

    return redirect(url_for('orders'))

