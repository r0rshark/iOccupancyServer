from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import db




class Locations(db.Model):
    __tablename__="location"
    id_device = db.Column(db.String(255), primary_key=True)
    id_beacon = db.Column(db.String(255))


    def __init__(self, id_device, id_beacon):
        self.id_device = id_device
        self.id_beacon = id_beacon


class BeaconLocations(db.Model):
    __tablename__="beacon_location"
    id_beacon = db.Column(db.String(255), primary_key=True)
    id_location = db.Column(db.String(255))


    def __init__(self, id_beacon, id_location):
        self.id_location = id_location
        self.id_beacon = id_beacon

    def __repr__(self):
        return '<BeaconLocations %r>' % self.id





