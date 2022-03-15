from app import db
from datetime import datetime


class BusaryStaff(db.Model):

    __tablename__ = 'busary_staff'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(200), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    pwd = db.Column(db.String(300), nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    services = db.relationship('Service', backref='staff', passive_deletes=True)

    @staticmethod
    def auth(email: str, pwd: str):
        _staff = BusaryStaff.query.filter_by(email=email, pwd=pwd).first()

        return _staff

    @staticmethod
    def add(name, email, pwd):
        _staff = BusaryStaff(name=name, email=email, pwd=pwd)

        db.session.add(_staff)
        db.session.commit()

        return _staff

    @staticmethod
    def change_pwd(staff_id: int, pwd: str):
        _staff: BusaryStaff = BusaryStaff.query.get(staff_id)

        if _staff is not None:
            _staff.pwd = pwd
            db.session.commit()

        return _staff
