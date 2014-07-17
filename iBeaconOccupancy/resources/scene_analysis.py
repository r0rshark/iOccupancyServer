
from flask import Flask, request, jsonify
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from iBeaconOccupancy.model.beacons  import *
from ..machine_learning import machine_learning

class deviceFullLogic(Resource):


    def delete(self,device):

     #deleting row in table location

      location = Locations.query.filter_by(id_device=device).first()
      if location is None:
          return "no location with this characteristic"
      db.session.delete(location)
      db.session.commit()

      return "OK"



    def post(self,device):
      req = request.json


      test_data = []
      info ={}
      for information in req:
        info[information['id_beacon']]=information['distance']
      test_data.append(info)


      mytest=[{'e2c56db5-dffb-48d2-b060-d0f5a71096e0035' : 9.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':1.93}]
      prediction = machine_learning.find_best_room(test_data)


      db.session.merge(Locations(device,prediction))
      db.session.commit()
      return "OK"



