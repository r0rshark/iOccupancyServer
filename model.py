
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Location(Base):
    __tablename__ = 'location'
    id_device = Column(String(255),primary_key=True)
    id_beacon = Column(String(255),primary_key=True)
    status =  Column(Integer)
    power =  Column(Integer)

    def __init__(self, id_device, id_beacon,status,power):
        self.id_device = id_device
        self.id_beacon = id_beacon
        self.status = status
        self.power = power

    def __repr__(self):
        return '<iBeacon %r>' % self.id

