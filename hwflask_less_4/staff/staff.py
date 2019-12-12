from flask import request, session
from flask_restful import Resource, marshal_with, reqparse
from db import db
from staff.staff_structure import staff_structure
from models.model import StaffModel
import json


parser = reqparse.RequestParser()
parser.add_argument('passport_id, type=str')

class Staf_f(Resource):
    @marshal_with(staff_structure)
    def get(self, value=None):
        passport_id = parser.parse_args()
        if value:
            data = StaffModel.query.get(value)
            return data
        elif passport_id:
            if StaffModel.passport_id == passport_id:
                return StaffModel.query.all()
        else:
            return StaffModel.query.all()

    def post(self):
        data = json.loads(request.data)
        if db.session.query(StaffModel).filter(StaffModel.passport_id == data['passport_id']).first():
            return "Room already exist"
        new_staff = StaffModel(**data)
        db.session.add(new_staff)
        db.session.commit()
        return "Added new staff"


    def patch(self,passport_id=None):
        if passport_id:
            new_data = request.json
            data = StaffModel.query.get(passport_id)
            if data:
                data.name = new_data.get('name')
                data.position = new_data.get('position')
                data.salary = new_data.get('salary')
                db.session.commit()
                return 'update '

    def delete(self,value=None):
        if value:
            staff = StaffModel.query.get(value)
            if staff:
                db.session.delete(staff)
                db.session.commit()
                return 'Delete room'

