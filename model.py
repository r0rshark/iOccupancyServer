from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

user="Laravel"
password="password"
host="127.0.0.1"
database="Ibeacon"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+":"+password+"@"+host+"/"+database
db = SQLAlchemy(app)


class Location(db.Model):
    __tablename__ = 'location'
    id_device = db.Column(db.String(255), primary_key=True)
    id_beacon = db.Column(db.String(255), primary_key=True)
    status =  db.Column(db.Integer)
    power =  db.Column(db.Integer)

    def __init__(self, id_device, id_beacon,status,power):
        self.id_device = id_device
        self.id_beacon = id_beacon
        self.status = status
        self.power = power

    def __repr__(self):
        return '<User %r>' % self.id_device
