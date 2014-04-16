from flask import Flask, request, jsonify
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from model import Location,db


app = Flask(__name__)



class Ibeacon(Resource):

  def post(self,device,beacon):
    req = request.json
    fields= ["status","power"]

    if not request.json or not  all(field in request.json for field in fields):
      print("POST with uncorrect fields")
      return "specify all field: status,power"

    db.session.merge(Location(device, beacon,req["status"],req["power"]))
    db.session.flush()
    db.session.commit()
    return "OK"

  def get(self, device,beacon):
      print "dev:"+device+"beacon"+beacon
      local = Location.query.filter_by(id_device=device,id_beacon=beacon).first()
      if local is None:
        return "no result with this id"
      return {"status": local.status,"power":local.power}

  def delete(self, device,beacon):
    location =Location.query.filter_by(id_device=device,id_beacon=beacon)
    if location is None:
      return "no location with this characteristic"
    db.session.delete(location)
    return "OK"

class Device(Resource):
    def get(self,device):
      locations =Location.query.filter_by(id_device=device).all()
      list_beacon = []
      for local in locations:
        list_beacon.append({"id_device":local.id_device, "id_beacon":local.id_beacon, "status": local.status,"power":local.power})
      return jsonify(results=list_beacon)



    def delete(self,device):
      locations =Location.query.filter_by(id_device=device).all()
      for loc in locations:
        db.session.delete(loc)
      db.session.commit()

      return "OK"


