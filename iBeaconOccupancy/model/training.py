from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from model import db



#----------------------Training-----------------------

class TrainingData(db.Model):
    __tablename__ = 'trainingdata'
    id = db.Column(db.Integer, primary_key=True)
    id_beacon = db.Column(db.String(255))
    distance =  db.Column(db.Float)
    rilevation =  db.Column(db.Integer,db.ForeignKey('trainingresult.id'))

    def __repr__(self):
        return '<Training %r>' % self.id


class TrainingResult(db.Model):
    __tablename__ = 'trainingresult'
    id= db.Column(db.Integer, primary_key=True)
    outcome = db.Column(db.String(255))
    data = db.relationship("TrainingData",backref="result")





