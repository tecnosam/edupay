from app import db
from datetime import datetime


neutral_status = ['PROCESSING', 'COLLECTED']
positive_status = ['APPROVED', 'READY']
negative_status = ['DISAPPROVED', 'CANCELLED']


class Status(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    tag = db.Column(db.String(20), unique=True, nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    orders = db.relationship('Order', backref='status', passive_deletes=True)
