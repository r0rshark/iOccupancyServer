#Flask server for iBeacon Occupancy Detection
##General Description

Server side application of Occupancy detection via iBeacon on Android devices project: system which exploits the iBeacon technology to make indoor position detection.
The server **collects the data** coming from the Android devices (set of approximated distances from the iBeacon transmitters located in different positions) to **create a model through the Support Vector Machines** methods in order to **determine in which room the device is located**.


##Installation Guide:

#### Environment Setup
* Download virtualenv: ```sudo apt-get install python-virtualenv```
* Run virtualenv inside the projec folder: ```virtualenv venv```
* Activate virtualenv: ```. venv/bin/activate```
* Download other usefull library: ```libmysqlclient-dev  python-dev  gfortran  libblas-dev liblapack-dev```
* If you are using a raspberry in order to install the follow requirements you have to give to compiler all ram, otherwise you cannot compile them. To do this open a terminal and with root privileges launch "raspi-config". On the screen select "Advance options" → "Memory split" → set "16" as memory for the gpu. After compiling you can restore the previous value.
* Install python packages: ```pip install -r requirements.txt```

#### Create  the database:
* Launch mysqld if not active
* Start  virtualenv with this command: ```. venv/bin/activate```
* Create a mysql user  and  a  database
* Check the fields  user password host  database in iBeaconOccupancy/model/config.py
* Create database  through script: ```./create_database.sh```

####Server Startup
* Launch the server with sudo because runs over port 80: ```sudo ./start_server.sh```

NB
All scripts must be modified with "chmod +x". If you want to change the port listening by the server just change the port number variable in tornado_laucher.py

###Dependecies Information
- SQLAlchemy:  libmysqlclient-dev e  python-dev
- scipy:  gfortran  libblas-dev liblapack-dev if any problem http://scikit-learn.org/stable/install.html
- matplotlib:  libfreetype6-dev libjpeg8-dev libpng-dev


Library needed may vary depending on the type and the version of the operationg system so don't completely rely on them probably in your system are required slightly different library

###Folder stucture
- app.py: app which start the default python server
- tornado_launcher.py: wrapper of app.py which allowes to run the server through Tornado
- iBeaconOccupancy: package which contains all the logic of the server
- test_machine_learning: contains a script used to test parameters and quality of the model found
- templates:simple html pages to show some information
