from flask import Flask, render_template, request, jsonify
from model import  Location
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import  Api
from resources import Ibeacon


# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Laravel:password@127.0.0.1/Ibeacon'
db = SQLAlchemy(app)

api = Api(app)
api.add_resource(Ibeacon, '/ibeacon/<string:id_device>/<string:id_beacon>')





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
