1)download virtualenv: sudo apt-get install python-virtualenv
  -launch virtualenv inside project folder: virtualenv venv
  -start virtualenv: . venv/bin/activate
  -install other library: bluez  libbluetooth-dev  python-bluez
  -to install other dependencies pip install -r requirements.txt
  -set the ip address and the port of the server in order to send http requests in bluetooth_server.py
  -set the number of users can be listened in bluetooth_server.py
  -in /etc/bluetooth/main.conf add this line "DisablePlugins = pnat"
  -copy the file hcid.conf in the same folder

Note sulle dipendenze
pybluez        => bluez  libbluetooth-dev  python-bluez
