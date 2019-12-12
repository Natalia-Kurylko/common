from flask import Blueprint
from flask_restful import Api
from staff.staff import Staf_f

staff_b = Blueprint('staff', __name__)
api = Api(staff_b)

api.add_resource(Staf_f, '/staff', '/staff/<value>')