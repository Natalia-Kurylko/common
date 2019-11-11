from flask import Flask, request, Blueprint
from flask_restful import Api, fields, Resource, reqparse, marshal_with

app = Flask(__name__)
staff_b = Blueprint('staff', __name__)
api = Api(staff_b)


class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staff_structure = {'name': fields.String,
                   'passport_id': fields.String,
                   'position': fields.String,
                   'salary': fields.Integer}

staff = [Staff('Jack', 'AA1111', 'waiter', 100), Staff('Julia', 'AA2222', 'cook', 120)]

parser = reqparse.RequestParser()
parser.add_argument('passport_id', type=str, help="Must have a staff passport_id.")


class Staf_f(Resource):
    @marshal_with(staff_structure)
    def get(self):
        args = parser.parse_args()
        if args['passport_id']:
            for p_id in staff:
                if p_id.passport_id == args['passport_id']:
                    return p_id
        return staff

    @marshal_with(staff_structure)
    def patch(self):
        name = request.args.get('name')
        passport_id = request.args.get('passport_id')
        position = request.args.get('position')
        salary = request.args.get('salary')
        for i in staff:
            if i.passport_id == passport_id:
                staff.remove(i)
        staff.append(Staff(name, passport_id, position, salary))
        return staff

    @marshal_with(staff_structure)
    def delete(self):
        rooms_copy = staff.copy()
        rooms_copy = [r for r in rooms_copy if r.passport_id != str(request.args.get('passport_id'))]
        return rooms_copy


api.add_resource(Staf_f, '/staff', '/staff/<value>')

if __name__ == '__main__':
    app.run(debug=True)
