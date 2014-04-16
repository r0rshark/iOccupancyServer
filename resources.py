from flask import Flask, request
from flask.ext.restful import Resource
from flask_sqlalchemy import SQLAlchemy
from model import Location,db


app = Flask(__name__)



class Ibeacon(Resource):

  def post(self,id_device,id_beacon):
    beacon = request.json
    fields= ["status","power"]

    if not request.json or not  all(field in request.json for field in fields):
      print("POST with uncorrect fields")
      return "specify all field: status,power"

    db.session.merge(Location(id_device, id_beacon,beacon["status"],beacon["power"]))
    db.session.flush()
    db.session.commit()
    return "OK"

  def get(self, id_device,id_beacon):
      return {id_beacon: id_device}

   # def put(self, todo_id):
     #   todos[todo_id] = request.form['data']
       # return {todo_id: todos[todo_id]}



