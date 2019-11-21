from flask import Flask, request, Blueprint
from flask_restful import Api, fields, Resource, reqparse, marshal_with


app = Flask(__name__)
room_b = Blueprint('rooms', __name__)
api = Api(room_b)


class Room:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


room_structure = {'number': fields.Integer,
                  'level': fields.String,
                  'status': fields.String,
                  'price': fields.Integer}

rooms = [Room(1, 'first', 'closed', 1000), Room(2, 'second', 'available', 2000)]

parser = reqparse.RequestParser()
parser.add_argument('number', type=int, help='Number should be integer')
parser.add_argument('status', type=str, help='Status should be string - "closed" or "available"')


class Rooms(Resource):
    @marshal_with(room_structure)
    def get(self):
        args = parser.parse_args()
        if args['number']:
            for n in rooms:
                if n.number == args['number']:
                    return n
        elif args['status']:
            ls = []
            for s in rooms:
                if s.status == args['status']:
                    ls.append(s)
            return ls
        return rooms

    @marshal_with(room_structure)
    def post(self):
        number = request.args.get('number')
        level = request.args.get('level')
        status = request.args.get('status')
        price = request.args.get('price')
        rooms.append(Room(number, level, status, price))
        return rooms

    @marshal_with(room_structure)
    def patch(self):
        number = request.args.get('number')
        level = request.args.get('level')
        status = request.args.get('status')
        price = request.args.get('price')
        for i in rooms:
            if i.number == number:
                rooms.remove(i)
        rooms.append(Room(number, level, status, price))
        return rooms

    @marshal_with(room_structure)
    def delete(self,value):
        for r in rooms:
            if r.number == int(value):
                rooms.remove(r)
                return 'delete'
        return 'no room'


api.add_resource(Rooms, '/rooms', '/rooms/<value>')

if __name__ == '__main__':
    app.run(debug=True)
