from flask import Flask, request, jsonify
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from iBeaconOccupancy.model.beacons  import *
from iBeaconOccupancy.model.tests  import *
from ..machine_learning import machine_learning
from datetime import datetime
import pprint as pr



class testBasic(Resource):
  def post(self):
    req = request.json
    fields= ["answer","strongest","correct"]
    #checking correctness of post message
    if not request.json or not  all(field in request.json for field in fields):
      print("POST with uncorrect fields")
      return "specify all field: answer,strongest,correct"

    #adding beacon to the beacons table

    db.session.merge(Tests(req["answer"],req["strongest"],req["correct"],datetime.now()))
    db.session.flush()
    db.session.commit()

    return "OK"

class testLearning(Resource):
  def post(self):

    req = request.json
    fields= ["answer","data"]

    #checking correctness of post message
    if not request.json or not  all(field in request.json for field in fields):
      print("POST with uncorrect fields")
      return "specify all field: answer,strongest,correct"

    information = req["data"]

    test_data = []
    info ={}
    for dat in information:
      info[dat['id_beacon']]=dat['distance']

    test_data.append(info)


    prediction = machine_learning.find_best_room(test_data)
    print "prediction "+str(prediction)
    print "answer "+req["answer"]


    #checking if it is correct
    if (prediction ==  req["answer"]):
      print "correct"
      correct =True
    else :
      print "wrong"
      correct=False


    #adding beacon to the beacons table

    db.session.merge(TestsLearning(req["answer"],prediction,correct,datetime.now()))
    db.session.flush()
    db.session.commit()

    return "OK"

class testClientFinal(Resource):
  def post(self):
    req = request.json
    fields= ["answer","strongest","correct"]
    #checking correctness of post message
    if not request.json or not  all(field in request.json for field in fields):
      print("POST with uncorrect fields")
      return "specify all field: answer,strongest,correct"

    #adding beacon to the beacons table



    db.session.merge(TestsClient(req["answer"],req["strongest"],req["correct"],datetime.now()))
    db.session.flush()
    db.session.commit()

    return "OK"

