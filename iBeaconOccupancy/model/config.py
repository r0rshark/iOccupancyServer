from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


user="Laravel"
password="password"
host="127.0.0.1"
database="Ibeacon"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+":"+password+"@"+host+"/"+database
db = SQLAlchemy(app)







