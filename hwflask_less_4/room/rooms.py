from flask import request
from flask_restful import Resource, marshal_with, reqparse
from db import db
from room.room_structure import room_structure
from models.model import RoomModel
import json


parser = reqparse.RequestParser()
parser.add_argument('number', type=int, help='Number should be integer')
parser.add_argument('status', type=str, help='Status should be string - "closed" or "available"')


class Rooms(Resource):
    @marshal_with(room_structure)
    def get(self, value=None):
        status = parser.parse_args()
        if value:
            data = RoomModel.query.get(value)
            return data
        elif status:
            if RoomModel.status==status:
                 return RoomModel.query.all()
        else:
            return RoomModel.query.all()

    def post(self):
        data = json.loads(request.data)
        if db.session.query(RoomModel).filter(RoomModel.number == data['number']).first():
            return "Room already exist"
        new_room = RoomModel(**data)
        db.session.add(new_room)
        db.session.commit()
        return 'Added new room'

    def patch(self, value=None):
        if value:
            new_room = request.json
            room = RoomModel.query.get(value)
            if room:
                room.level = new_room.get('level')
                room.status = new_room.get('status')
                room.price = new_room.get('price')
                room.tenant_id = new_room.get('tenant_id')
                db.session.commit()
                return 'Updated'

    def delete(self, value=None):
        if value:
            room = RoomModel.query.get(value)
            if room:
                db.session.delete(room)
                db.session.commit()
                return 'Delete room'
