from app import db
from datetime import datetime


class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'))

    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))

    status_id = db.Column(db.Integer, db.ForeignKey('status.id', ondelete='CASCADE'))

    date_created = db.Column(db.DateTime, default=datetime.utcnow())
