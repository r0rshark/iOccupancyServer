from flask import Flask, render_template, request, jsonify
from model import  Location
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import  Api
from resources import Ibeacon
from model import db


# Initialize the Flask application

app = Flask(__name__)


api = Api(app)
api.add_resource(Ibeacon, '/ibeacon/<string:device>/<string:beacon>')


@app.before_first_request
def setup():
    app.debug = True
    # Recreate database each time for demo




@app.route('/')
def index():

  # Render template
  locations = db.session.query(Location).all()
  return render_template('request.html', data=locations)






# Run
if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 8000
    )
