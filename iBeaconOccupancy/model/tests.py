from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from model import db



#---------------------TEST------------------------


class Tests(db.Model):
    __tablename__ = "tests_basic"
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(255))
    strongest = db.Column(db.String(255))
    correct = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self,answer,strongest,correct,date):
        self.answer = answer
        self.strongest = strongest
        self.correct = correct
        self.date = date


class TestsClient(db.Model):
    __tablename__ = "tests_client"
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(255))
    strongest = db.Column(db.String(255))
    correct = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self,answer,strongest,correct,date):
        self.answer = answer
        self.strongest = strongest
        self.correct = correct
        self.date = date

class TestsLearning(db.Model):
    __tablename__ = "tests_learning"
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(255))
    strongest = db.Column(db.String(255))
    correct = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self,answer,strongest,correct,date):
        self.answer = answer
        self.strongest = strongest
        self.correct = correct
        self.date = date

