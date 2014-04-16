from flask import Flask, request
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

   # def put(self, todo_id):
     #   todos[todo_id] = request.form['data']
       # return {todo_id: todos[todo_id]}



