from flask import Blueprint
from flask_restful import Api
from tenants.tenant import Tenants


tenants_b = Blueprint('tenants', __name__)
api = Api(tenants_b)

api.add_resource(Tenants, '/tenants', '/tenants/<value>')
