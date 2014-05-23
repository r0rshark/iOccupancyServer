from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

user="Laravel"
password="password"
host="127.0.0.1"
database="Ibeacon"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+":"+password+"@"+host+"/"+database
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(255),primary_key=True)
    password = db.Column(db.String(512))

class Beacons(db.Model):
    __tablename__ = 'beacons'
    id_device = db.Column(db.String(255), primary_key=True)
    id_beacon = db.Column(db.String(255), primary_key=True)
    status =  db.Column(db.Integer)
    power =  db.Column(db.Integer)
    user = db.Column(db.String(255))
    last_update = db.Column(db.DateTime)

    def __init__(self, id_device, id_beacon,status,power,user,last_update):
        self.id_device = id_device
        self.id_beacon = id_beacon
        self.status = status
        self.power = power
        self.user = user
        self.last_update = last_update


    def __repr__(self):
        return '<User %r>' % self.id_device

class Locations(db.Model):
    __tablename__="location"
    id_device = db.Column(db.String(255), primary_key=True)
    id_beacon = db.Column(db.String(255))
    user = db.Column(db.String(255))

    def __init__(self, id_device, id_beacon, user):
        self.id_device = id_device
        self.id_beacon = id_beacon
        self.user = user

class Tests(db.Model):
    __tablename__ = "tests"
    answer = db.Column(db.String(255), primary_key=True)
    strongest = db.Column(db.String(255), primary_key=True)
    correct = db.Column(db.Integer)
    date = db.Column(db.DateTime, primary_key=True)

    def __init__(self,answer,strongest,correct,date):
        self.answer = answer
        self.strongest = strongest
        self.correct = correct
        self.date = date

