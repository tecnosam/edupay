from flask_restful import fields


order_fields = {
    'id': fields.Integer,
    'status_id': fields.Integer,

    'status': fields.Nested({
        'id': fields.Integer,
        'tag': fields.String
    }),

    'service': fields.Nested({
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

service_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'date_created': fields.DateTime,
}

student_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'matric': fields.String,
    'date_created': fields.DateTime
}

staff_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}
