from app import db
from datetime import datetime


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    uploaded_by = db.Column(db.Integer, db.ForeignKey('busary_staff.id', ondelete='CASCADE'))

    name = db.Column(db.String(200), unique=True, nullable=False)

    price = db.Column(db.Float, nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    orders = db.relationship('Order', backref='product', passive_deletes=True)

    @staticmethod
    def add(name, price, uploaded_by):
        _product = Product(name=name, price=price, uploaded_by=uploaded_by)

        db.session.add(_product)
        db.session.commit()

        return _product
    
    @staticmethod
    def edit(product_id: int, name=None, price=None):
        _product: Product = Product.query.get(product_id)

        if _product is not None:
            print(name, price, "mk")
            if name is not None:
                _product.name = name

            if price is not None:
                _product.price = price

        db.session.commit()

        return _product
    
    @staticmethod
    def delete(product_id: int):
        _product: Product = Product.query.get(product_id)

        if _product is not None:

            db.session.delete(_product)

            db.session.commit()
        
        return _product
