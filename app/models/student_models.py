from app import db
from datetime import datetime

from hashlib import sha256


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(200), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    matric = db.Column(db.String(20), unique=True, nullable=False)

    pwd = db.Column(db.String(300), nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    orders = db.relationship('Order', backref='student', passive_deletes=True)

    @staticmethod
    def auth(matric: str, pwd: str):
        _pwd = sha256(pwd.encode()).hexdigest()
        _student = Student.query.filter_by(matric=matric, pwd=_pwd).first()

        return _student

    @staticmethod
    def add(name: str, email: str, matric: str, pwd: str):
        _pwd = sha256(pwd.encode()).hexdigest()
        _student = Student(name=name, email=email, matric=matric, pwd=_pwd)

        db.session.add(_student)
        db.session.commit()

        return _student

    @staticmethod
    def change_pwd(student_id: int, pwd: str):
        _student: Student = Student.query.get(student_id)

        if _student is not None:
            _pwd = sha256(pwd.encode()).hexdigest()

            _student.pwd = _pwd
            db.session.commit()

        return _student
