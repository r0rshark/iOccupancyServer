from flask import Flask, render_template, request, jsonify
from model import Base, Location
from flask_sqlalchemy import SQLAlchemy


# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Laravel:password@127.0.0.1/Ibeacon'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    app.debug = True
    # Recreate database each time for demo
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)



@app.route('/')
def index():

    # Render template
    locations = db.session.query(Location).all()
    for loc in locations:
      print loc.id_device+" "+loc.id_beacon
    return render_template('request.html', data=locations)

@app.route('/ibeacon', methods = ['GET'])
def getIBeacon():
  locations = db.session.query(Location).all()
  return jsonify(locations)


@app.route('/ibeacon', methods = ['POST'])
def post():
  beacon = request.json
  fields= ["id_device","id_beacon","status","power"]
  if not request.json or not  all(field in request.json for field in fields):
    return "specify all field: id_device,id_beacon,status,power"

  print("fewfwe")
  local = Location.query.get(1)
  print("beacodasdsa")
  if local is None:
    db.session.add(Location(beacon["id_device"], beacon["id_beacon"],beacon["status"],beacon["power"]))
  else:
    local.status=beacon["status"]
    local.power=beacon["power"]


  #db.session.merge(Location(id_device=beacon["id_device"],id_beacon=beacon["id_ibeacon"]))
  db.session.commit()
  return "OK"





# Run
if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 8000
    )
