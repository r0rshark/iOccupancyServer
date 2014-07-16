from flask import Flask, request, jsonify
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from iBeaconOccupancy.model.beacons  import *
from ..machine_learning import machine_learning

class deviceFullLogic(Resource):
    def get(self,device):
      locations =Beacons.query.filter_by(id_device=device).all()
      list_beacon = []
      for local in locations:
        list_beacon.append({"id_device":local.id_device, "id_beacon":local.id_beacon, "status": local.status,"power":local.power,"user":local.user,"last_update":local.last_update})
      return jsonify(results=list_beacon)



    def delete(self,device):
       #deleting all rows in table beacons
      beacons =Beacons.query.filter_by(id_device=device).all()
      for loc in beacons:

        db.session.delete(loc)
     #deleting row in table location

      location = Locations.query.filter_by(id_device=device).first()
      if location is None:
          return "no location with this characteristic"
      db.session.delete(location)
      db.session.commit()

      return "OK"



    def post(self,device):
      req = request.json

      '''
      print req[0]['id_beacon']
      fields= ["id_beacon","status","power","user"]
      # checking correctness of post message
      if not request.json or not  all(field in request.json for field in fields):
        print("POST with uncorrect fields")
      return "specify all field: id_beacon,user,status,power"
      '''
      test_data = []
      info ={}
      for information in req:
        info[information['id_beacon']]=information['distance']
      test_data.append(info)


      mytest=[{'e2c56db5-dffb-48d2-b060-d0f5a71096e0035' : 9.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':1.93}]
      prediction = machine_learning.find_best_room(test_data)

      #adding beacon to the beacons table
      #db.session.merge(Beacons(device, req["id_beacon"],req["status"],req["power"],req["user"],datetime.now()))
      #db.session.flush()
      #db.session.commit()

      #deleting old Beacons
      #beacons =Beacons.query.filter_by(id_device=device).all()
      #survived_beacons = self.refreshingBeacons(beacons)


      #stronger_beacon = self.chooseBestLocation(survived_beacons)

      db.session.merge(Locations(device,prediction))
      db.session.commit()
      return "OK"



