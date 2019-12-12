from flask import request
from flask_restful import Resource, marshal_with, reqparse
from db import db
from tenants.tenant_structure import tenants_structure
from models.model import TenantModel
import json


parser = reqparse.RequestParser()
parser.add_argument('passport_id, type=str')


class Tenants(Resource):
    @marshal_with(tenants_structure)
    def get(self, value=None):
        passport_id = parser.parse_args()
        if value:
            data = TenantModel.query.get(value)
            return data
        elif passport_id:
            if TenantModel.passport_id == passport_id:
                return TenantModel.query.all()
        else:
            return TenantModel.query.all()

    def patch(self, passport_id):
        if passport_id:
            new_data = request.json
            data = TenantModel.query.get(passport_id)

            data.name = new_data.get('name')
            data.age = new_data.get('age')
            data.sex = new_data.get('sex')
            data.address = new_data.get('address')
            db.session.commit()
            return 'update '

    def delete(self, value):
        if value:
            tenant = TenantModel.query.get(value)
            if tenant:
                db.session.delete(tenant)
                db.session.commit()
                return 'Delete room'
