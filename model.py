from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

user="Laravel"
password="password"
host="127.0.0.1"
database="Ibeacon"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+":"+password+"@"+host+"/"+database
db = SQLAlchemy(app)


class Beacons(db.Model):
    __tablename__ = 'beacons'
    id_device = db.Column(db.String(255), primary_key=True)
    id_beacon = db.Column(db.String(255), primary_key=True)
    status =  db.Column(db.Integer)
    power =  db.Column(db.Integer)
    last_update = db.Column(db.DateTime)

    def __init__(self, id_device, id_beacon,status,power,last_update):
        self.id_device = id_device
        self.id_beacon = id_beacon
        self.status = status
        self.power = power
        self.last_update = last_update


    def __repr__(self):
        return '<User %r>' % self.id_device

class Locations(db.Model):
    __tablename__="location"
    id_device = db.Column(db.String(255), primary_key=True)
    id_beacon = db.Column(db.String(255))

    def __init__(self, id_device, id_beacon):
        self.id_device = id_device
        self.id_beacon = id_beacon

