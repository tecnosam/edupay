from app import db
from datetime import datetime


class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    service_id = db.Column(db.Integer, db.ForeignKey('service.id', ondelete='CASCADE'))

    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))

    status_id = db.Column(db.Integer, db.ForeignKey('status.id', ondelete='CASCADE'), default=1)

    paystack_ref = db.Column(db.String(30), unique=True, nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    @staticmethod
    def add(service_id, student_id, paystack_ref):
        _order = Order(service_id=service_id, student_id=student_id, paystack_ref=paystack_ref)

        db.session.add(_order)
        db.session.commit()

        return _order
    
    @staticmethod
    def change_status(service_id, status_id):
        _order: Order = Order.query.get(service_id)

        if _order is not None:
            _order.status_id = status_id

            db.session.commit()

        return _order
