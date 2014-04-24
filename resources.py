from flask import Flask, request, jsonify
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from model import Beacons,db,Locations
from datetime import datetime



app = Flask(__name__)



class beaconMinimalLogic(Resource):

  def post(self,device,beacon):
    req = request.json

    db.session.merge(Locations(device, beacon))
    db.session.flush()
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
      locations =Beacons.query.filter_by(id_device=device).all()
      for loc in locations:
        db.session.delete(loc)
      db.session.commit()

      return "OK"

class beaconFullLogic(Resource):

  def post(self,device,beacon):
    req = request.json
    fields= ["status","power"]

    if not request.json or not  all(field in request.json for field in fields):
      print("POST with uncorrect fields")
      return "specify all field: status,power"

    beacons =Beacons.query.filter_by(id_device=device).all()
    dt = datetime.now()


    for ibeac in beacons:
      if dt.microsecond - ibeac.last_update.microsecond > 5:
        db.session.delete(ibeac)
    db.session.commit()

    if all(req["power"] > beac.power for beac in beacons):
      print "inside if"
      db.session.merge(Locations(device,beacon))
      db.session.flush()
      db.session.commit()

    db.session.merge(Beacons(device, beacon,req["status"],req["power"],datetime.now()))
    db.session.flush()
    db.session.commit()
    return "OK"



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








