1)scaricare virtualenv: sudo apt-get install python-virtualenv
  -lanciare virtualenv nella cartella edl progetto: virtualenv venv
  -attivare virtualenv: . venv/bin/activate
  -in ubuntu è stato necessario installare: libmysqlclient-dev  python-dev  gfortran  libblas-dev liblapack-dev
  -per installare le restanti dipendenze pip install -r requirements.txt

2) creare il database:
  - avviare mysqld se non è gia attivo
  -avviare il virtualenv con questo comando: . venv/bin/activate
  -creare un utente mysql e associarlo a un database
  -controllare i campi user password host e database in iBeaconOccupancy/model.py
  -lanciare lo script ./create_database.sh
3)lanciare il server lanciare lo script start_server.sh

Note sulle dipendenze
SQLAlchemy =>  libmysqlclient-dev e  python-dev
scipy            =>  gfortran  libblas-dev liblapack-dev
matplotlib    =>  libfreetype6-dev libjpeg8-dev libpng-dev
pybluez        => bluez  libbluetooth-dev  python-bluez
poi pip install pybluez
