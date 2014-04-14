from flask import Flask, render_template, request, jsonify
from model import Base, Location
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Laravel:password@127.0.0.1/Ibeacon'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    # Recreate database each time for demo
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.add(Location('Bob Jones', 'bobom',12,32))
    db.session.add(Location('Joe Quimby', 'eat@joes.com',123,54))
    db.session.commit()


@app.route('/')
def index():

    # Render template
    locations = db.session.query(Location).all()
    for loc in locations:
      print loc.id_device+" "+loc.id_beacon

    return render_template('request.html', data=locations)

@app.route('/post', methods = ['POST'])
def post():

    # Get the parsed contents of the form data
    json = request.json
    print(json)
    # Render template
    return jsonify(json)

# Run
if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 8000
    )
