1)download virtualenv: sudo apt-get install python-virtualenv
  -run virtualenv inside the projec folder: virtualenv venv
  -activate virtualenv: . venv/bin/activate
  -download other usefull library: libmysqlclient-dev  python-dev  gfortran  libblas-dev liblapack-dev
  -install python packages: pip install -r requirements.txt

2) create   database:
  - launch mysqld if not active
  -start  virtualenv with this command: . venv/bin/activate
  -create a mysql user  and  a  database
  -check the fields  user password host  database in iBeaconOccupancy/model/config.py
  -create database  through script: ./create_database.sh
3)launch the server with sudo because runs over port 80: ./start_server.sh

Library notes
SQLAlchemy =>  libmysqlclient-dev e  python-dev
scipy            =>  gfortran  libblas-dev liblapack-dev if any problem http://scikit-learn.org/stable/install.html
matplotlib    =>  libfreetype6-dev libjpeg8-dev libpng-dev


Library needed may vary depending on the type and the version of the operationg system so don't completely rely on them probably in yourr system are required slightly different library

Folder stucture
app.py: app which start the default python server
tornado_launcher.py: wrapper of app.py which allowes to run the server through Tornado
iBeaconOccupancy: package which contains all the logic of the server
test_machine_learning: contains a script used to test parameters and quality of the model found
templates:simple html pages to show some information
