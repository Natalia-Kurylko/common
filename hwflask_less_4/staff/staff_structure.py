from flask_restful import fields

staff_structure = {'name': fields.String,
                   'passport_id': fields.Integer,
                   'position': fields.String,
                   'salary': fields.Integer}
