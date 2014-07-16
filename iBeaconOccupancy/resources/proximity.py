from flask import Flask, request, jsonify
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from iBeaconOccupancy.model.beacons  import *




class beaconMinimalLogic(Resource):

  def post(self,device,beacon):

    print "recieved location" + beacon +"from "+device
    beaconloc = BeaconLocations.query.filter_by(id_beacon=beacon).first()
    room = beaconloc.id_location
    if room is  None:
      print "room not found in database BeaconLocations"
      return ""

    print "------  " + device +" -> "+room+"-----"

    db.session.merge(Locations(device, room))
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


