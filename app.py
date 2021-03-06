from flask import Flask, render_template, request, jsonify
from iBeaconOccupancy.model.beacons import  *
from iBeaconOccupancy.model.tests import  *
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import  Api
from iBeaconOccupancy.machine_learning import machine_learning
from iBeaconOccupancy.resources import *

#import bluetooth_server
import thread




# Initialize the Flask application

app = Flask(__name__)


api = Api(app)
api.add_resource(proximity.beaconMinimalLogic, '/ibeacon/<string:device>/<string:beacon>')
api.add_resource(proximity.deviceMinimalLogic, '/ibeacon/<string:device>')
api.add_resource(scene_analysis.deviceFullLogic, '/ibeaconserver/<string:device>')
api.add_resource(test.testBasic, '/ibeacon/test_basic')
api.add_resource(training.training,'/ibeacon/training')
api.add_resource(test.testLearning,'/ibeacon/testLearning')
api.add_resource(test.testClientFinal,'/ibeacon/testClient')


@app.before_first_request
def setup():
    app.debug = True






@app.route('/')
def location():

  # Render template
  local = db.session.query(Locations).all()
  return render_template('locations.html', data=local)

@app.route('/tests')
def tests():
  # Render template
  local = db.session.query(TestsLearning).all()
  return render_template('tests.html', data=local)

@app.route('/testsclient')
def testsclient():
  # Render template
  local = db.session.query(TestsClient).all()
  return render_template('tests.html', data=local)


def setup():
  machine_learning.load_data()




setup()
if __name__ == '__main__':

    app.run(

        host = "0.0.0.0",
        port = 80
    )



