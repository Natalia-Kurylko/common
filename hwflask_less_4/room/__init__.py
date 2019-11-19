from flask import Blueprint
from flask_restful import Api
from room.rooms import Rooms

room_b = Blueprint('rooms', __name__)
api = Api(room_b)

api.add_resource(Rooms, '/rooms', '/rooms/<value>')