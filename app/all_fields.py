from flask_restful import fields


order_fields = {
    'id': fields.Integer,
    'status_id': fields.Integer,

    'status': fields.Nested({
        'id': fields.Integer,
        'tag': fields.String
    }),

    'product': fields.Nested({
        'id': fields.Integer,
        'name': fields.String,
        'price': fields.Float
    }),

    'student': fields.Nested({
        'id': fields.Integer,
        'name': fields.String,
        'matric': fields.String
    }),

    'date_created': fields.DateTime
}

student_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'matric': fields.String,
    'orders': fields.Nested(order_fields),
    'date_created': fields.DateTime
}
