from datetime import timedelta
from flask import Flask
from flask_migrate import Migrate

from  config import run_config
from db import  db
from room import room_b
from  staff import staff_b
from tenants import tenants_b
from create_db import create_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    db.init_app(app)
    Migrate().init_app(app, db)
    app.permanent_session_lifetime = timedelta(minutes=20)  # add session expire time
    app.register_blueprint(room_b)
    app.register_blueprint(staff_b)
    app.register_blueprint(tenants_b)
    app.register_blueprint(create_db)
    return app



if __name__ == "__main__":
    create_app().run()