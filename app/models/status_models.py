import sqlalchemy
from app import db
from datetime import datetime


class Status(db.Model):

    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    tag = db.Column(db.String(20), unique=True, nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    orders = db.relationship('Order', backref='status', lazy=True, passive_deletes=True)

    @staticmethod
    def add(tag: str):
        try:
            _status = Status(tag=tag)
            db.session.add(_status)
            db.session.commit()
            return _status
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            return
