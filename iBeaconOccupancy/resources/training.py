
from flask import Flask, request, jsonify
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from iBeaconOccupancy.model.training import *
import pprint as pr


class training(Resource):

  def post(self):
    print "------Inserting info in Training Database----"
    req = request.json
    res = TrainingResult(outcome=req[0]['answer'])

    for information in req:
      info = TrainingData(id_beacon=information['id_beacon'],distance=information['distance'])
      res.data.append(info)


    db.session.add(res)
    for information in res.data:
      db.session.add(information)

    db.session.commit()


    return "ok"
