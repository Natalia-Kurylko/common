from flask import Flask, request, Blueprint
from flask_restful import Api, fields, Resource, reqparse, marshal_with

app = Flask(__name__)
tenants_b = Blueprint('tenants', __name__)
api = Api(tenants_b)


class Tenant:
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number


address_structure = {"city": fields.String,
                     "street": fields.String}

tenants_structure = {'name': fields.String,
                     'passport_id': fields.String,
                     'age': fields.Integer,
                     'sex': fields.String,
                     'address': fields.Nested(address_structure),
                     'room_number': fields.Integer}

tenants = [Tenant('Nata', 'AA2637', 27, 'woman', {'city': 'Zhytomyr', 'street': 'Peremohy 10'}, 107),
           Tenant('Sergey', 'AA9732', 27, 'men', {'city': 'Zhytomyr', 'street': 'Heroiv Desantnykiv 11'}, 108)]

parser = reqparse.RequestParser()
parser.add_argument('passport_id', type=str, help="Must have a staff passport_id.")


class Tenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        args = parser.parse_args()
        if args['passport_id']:
            for p_id in tenants:
                if p_id.passport_id == args['passport_id']:
                    return p_id
        return tenants

    @marshal_with(tenants_structure)
    def patch(self):
        name = request.args.get('name')
        passport_id = request.args.get('passport_id')
        age = request.args.get('age')
        sex = request.args.get('sex')
        address = request.args.get('address')
        room_number = request.args.get('room_number')
        for i in tenants:
            if i.passport_id == passport_id:
                tenants.remove(i)
        tenants.append(Tenant(name, passport_id, age, sex, address, room_number))
        return tenants

    @marshal_with(tenants_structure)
    def delete(self):
        tenants_copy = tenants.copy()
        tenants_copy = [t for t in tenants_copy if t.passport_id != str(request.args.get('passport_id'))]
        return tenants_copy


api.add_resource(Tenants, '/tenants', '/tenants/<value>')

if __name__ == '__main__':
    app.run(debug=True)
