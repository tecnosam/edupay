from app import db
from datetime import datetime


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(200), nullable=False)

    matric = db.Column(db.String(20), unique=True, nullable=False)

    pwd = db.Column(db.String(300), nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    orders = db.relationship('Order', backref='student', passive_deletes=True)

    @staticmethod
    def auth(matric: str, pwd: str):
        _student = Student.query.filter_by(matric=matric, pwd=pwd).first()

        return _student