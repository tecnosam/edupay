from app import db
from datetime import datetime


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(200), unique=True, nullable=False)

    price = db.Column(db.Float, nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    orders = db.relationship('Order', backref='product', passive_deletes=True)

    @staticmethod
    def add(name, price):
        _product = Product(name=name, price=price)

        db.session.add(_product)
        db.session.commit()

        return _product
