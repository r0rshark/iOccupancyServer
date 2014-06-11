Gli script a cui si fa riferimento sono nella cartella setup
1)scaricare virtualenv: sudo apt-get install python-virtualenv
  -lanciare virtualenv nella cartella edl progetto: virtualenv venv
  -attivare virtualenv: . venv/bin/activate
  -in ubuntu e stato necessario  sudo apt-get install libmysqlclient-dev e sudo apt-get install python-dev
  -per installare le restanti dipendenze pip install -r requirements.txt

2) creare il database:
  - avviare mysqld se non è gia attivo
  -avviare il virtualenv con questo comando: . venv/bin/activate
  -controllare i campi user password host e database in model.py
  -lanciare lo script ./create_database.sh
3)lanciare il server lanciare lo script start_server.sh
4)Per installare scipy brew install gfortran
5) per installare matplotlib in linux installare le dipendenze:apt-get install libfreetype6-dev libjpeg8-dev libpng-dev
6)bluetooth in linux installare bluez poi apt-get install libbluetooth-dev , python-bluez
  poi pip install pybluez
