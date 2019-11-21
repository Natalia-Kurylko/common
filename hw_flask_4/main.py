from flask import Flask
from  config import run_config
from blueprint.rooms import room_b
from blueprint.staff import staff_b
from blueprint.tenants import tenants_b

app = Flask(__name__)
app.config.from_object(run_config)

app.register_blueprint(room_b)
app.register_blueprint(staff_b)
app.register_blueprint(tenants_b)

if __name__ == "__main__":
    app.run(debug=True)