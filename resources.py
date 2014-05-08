from flask import Flask, request, jsonify
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from model import Beacons,db,Locations,Tests
from datetime import datetime



app = Flask(__name__)



class beaconMinimalLogic(Resource):

  def post(self,device,beacon):
    req = request.json
    db.session.merge(Locations(device, beacon))
    db.session.commit()
    return "OK"

  def get(self, device,beacon):
      print "dev:"+device+"beacon"+beacon
      local = Locations.query.filter_by(id_device=device,id_beacon=beacon).first()
      if local is None:
        return False
      return True

  def delete(self, device,beacon):
    loc =Locations.query.get(device)
    print loc
    if loc is None:
      return "no location with this characteristic"
    db.session.delete(loc)
    db.session.commit()
    return "OK"

class deviceMinimalLogic(Resource):
    def get(self,device):
      local =Locations.query.filter_by(id_device=device).first()
      return  {"id_device":local.id_device, "id_beacon":local.id_beacon}



    def delete(self,device):
      local =Locations.query.filter_by(id_device=device).first()
      if local is None:
        return "device not found"
      db.session.delete(local)
      db.session.commit()
      return "OK"


class deviceFullLogic(Resource):
    def get(self,device):
      locations =Beacons.query.filter_by(id_device=device).all()
      list_beacon = []
      for local in locations:
        list_beacon.append({"id_device":local.id_device, "id_beacon":local.id_beacon, "status": local.status,"power":local.power,"last_update":local.last_update})
      return jsonify(results=list_beacon)



    def delete(self,device):
       #deleting all rows in table beacons
      beacons =Beacons.query.filter_by(id_device=device).all()
      for loc in beacons:
        db.session.delete(loc)
     #deleting row in table location
      location = Locations.query.filter_by(id_device=device).first()
      db.session.delete(location)
      db.session.commit()

      return "OK"

class beaconFullLogic(Resource):

  def post(self,device,beacon):
    req = request.json
    fields= ["status","power"]
    #checking correctness of post message
    if not request.json or not  all(field in request.json for field in fields):
      print("POST with uncorrect fields")
      return "specify all field: status,power"

    #adding beacon to the beacons table
    db.session.merge(Beacons(device, beacon,req["status"],req["power"],datetime.now()))
    db.session.flush()
    db.session.commit()

    #deleting old beacons
    beacons =Beacons.query.filter_by(id_device=device).all()
    survived_beacons = self.refreshingBeacons(beacons)


    stronger_beacon = self.chooseBestLocation(survived_beacons)

    db.session.merge(Locations(stronger_beacon.id_device,stronger_beacon.id_beacon))
    db.session.commit()






    return "OK"

  def refreshingBeacons(self,beacons):
    dt = datetime.now()
    updated_beacons=[]
    print "beacons len"+ str(len(beacons))
    for ibeac in beacons:
      print "micro seconds "+str((dt - ibeac.last_update).seconds)
      if (dt - ibeac.last_update).seconds> 5:
        db.session.delete(ibeac)
      else:
        updated_beacons.append(ibeac)
    db.session.commit()
    return updated_beacons


  def chooseBestLocation(self,beacons):
    stronger_beacon = beacons[0]
    for beacon in beacons:
      if (beacon.power >= stronger_beacon.power):
        stronger_beacon = beacon
    return stronger_beacon


  def get(self, device,beacon):
      print "dev:"+device+"beacon"+beacon
      local = Beacons.query.filter_by(id_device=device,id_beacon=beacon).first()
      if local is None:
        return "no result with this id"
      return {"status": local.status,"power":local.power}

  def delete(self, device,beacon):
    location =Beacons.query.filter_by(id_device=device,id_beacon=beacon)
    if location is None:
      return "no location with this characteristic"
    db.session.delete(location)
    return "OK"


class test(Resource):
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







