from app import db
from datetime import datetime


class Service(db.Model):

    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    uploaded_by = db.Column(db.Integer, db.ForeignKey('busary_staff.id', ondelete='CASCADE'))

    name = db.Column(db.String(200), unique=True, nullable=False)

    price = db.Column(db.Float, nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    orders = db.relationship('Order', backref='service', passive_deletes=True)

    @staticmethod
    def add(name, price, uploaded_by):
        _service = Service(name=name, price=price, uploaded_by=uploaded_by)

        db.session.add(_service)
        db.session.commit()

        return _service
    
    @staticmethod
    def edit(service_id: int, name=None, price=None):
        _service: Service = Service.query.get(service_id)

        if _service is not None:
            print(name, price, "mk")
            if name is not None:
                _service.name = name

            if price is not None:
                _service.price = price

        db.session.commit()

        return _service
    
    @staticmethod
    def delete(service_id: int):
        _service: Service = Service.query.get(service_id)

        if _service is not None:

            db.session.delete(_service)

            db.session.commit()
        
        return _service
