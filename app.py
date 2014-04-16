from flask import Flask, render_template, request, jsonify
from model import  Location
from flask_sqlalchemy import SQLAlchemy


# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Laravel:password@127.0.0.1/Ibeacon'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    app.debug = True
    # Recreate database each time for demo




@app.route('/')
def index():

  # Render template
  locations = db.session.query(Location).all()
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
    print("POST with uncorrect fields")
    return "specify all field: id_device,id_beacon,status,power"

  db.session.merge(Location(beacon["id_device"], beacon["id_beacon"],beacon["status"],beacon["power"]))
  db.session.flush()
  db.session.commit()




  return "OK"





# Run
if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 80
    )
