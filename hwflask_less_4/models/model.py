from db import db

staff_rooms = db.Table(
    'staff_rooms',
    db.Column('passport_id', db.Integer, db.ForeignKey('staff.passport_id')),
    db.Column('number', db.Integer, db.ForeignKey('rooms.number'))
)


class RoomModel(db.Model):
    __tablename__ = "rooms"
    number = db.Column(db.Integer, primary_key=True, unique=True)
    level = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.passport_id'))



class TenantModel(db.Model):
    __tablename__ = 'tenants'
    passport_id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String)
    rooms = db.relationship('RoomModel', backref='tenants', lazy= True)

class StaffModel(db.Model):
    __tablename__ = 'staff'
    passport_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    salary = db.Column(db.String)
    serve = db.relationship('RoomModel', secondary=staff_rooms, backref=db.backref('serve'))
