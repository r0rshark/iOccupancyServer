from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


user=""
password=""
host=""
database=""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+":"+password+"@"+host+"/"+database
db = SQLAlchemy(app)







