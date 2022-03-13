from flask import render_template, redirect, request, url_for, session, flash
from app import flask_app

import sqlalchemy
from app.models.order_models import Order

from app.models.product_models import Product


@flask_app.route("/receipts")
def receipts():
    if 'staff_data' not in session:
        return redirect(url_for('staff_login'))

    return redirect(url_for('orders'))

@flask_app.route("/products", methods=['GET', 'POST'])
def products():

    if 'staff_data' not in session:
        return redirect(url_for('staff_login'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')

        method = request.form.get('_method', 'POST')

        try:

            if method.upper() =='PUT':
                product_id = request.form.get('id', 0)
                _product = Product.edit(product_id, name, price)

            else:
                _product = Product.add(name, price, session['staff_data']['id'])

            if _product is not None:
                flash("Successfully uploaded product/service")
            else:
                flash("There was an error locating this product")

        except sqlalchemy.exc.IntegrityError:
            print("oops")
            flash("A Product/Service with this name already exists")
    elif 'pop' in request.args:
        product_id = request.args['pop']
        _product = Product.delete(product_id)

        if _product is not None:
            flash("Successfully deleted product/service")
        else:
            flash("There was an error locating this product")


    products = Product.query.all()
    return render_template("pages/products.html", products=products)


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

