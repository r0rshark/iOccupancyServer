import bluetooth
import thread
import json
import requests
from socket import error as SocketError


name="bt_server"
target_name="siggen"
uuid="94f39d29-7d6d-437d-973b-fba39e49d4ee"
url_client_logic="http://192.168.0.105/ibeacon/"
url_server_logic="http://192.168.0.105/ibeaconserver/"
number_to_listen=2

def runServer():
    serverSocket=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
    port=bluetooth.PORT_ANY
    serverSocket.bind(("",port))
    print "Listening for connections on port: ", port
    serverSocket.listen(number_to_listen)
    port=serverSocket.getsockname()[1]

    bluetooth.advertise_service( serverSocket, "SampleServer",service_id = uuid,service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ], profiles = [ bluetooth.SERIAL_PORT_PROFILE ])


    while True:
        print "waiting connection"
        inputSocket, address=serverSocket.accept()
        print "address"+str(address)
        thread.start_new_thread( handle_client, (inputSocket, address ))



def handle_client(inputSocket,address):
    print "Spawing thread for " + str(address)
    inputSocket.settimeout(None)
    while True:
        try:
            myjson=inputSocket.recv(1024)


        except bluetooth.btcommon.BluetoothError as e:
            print "client "+str(address)+" has disconnected"
            inputSocket.close()
            return
            #time.sleep(0,001)


        if not myjson:
            break
        try:
            data = json.loads(myjson)
        except ValueError:
            continue

        print "["+str(address)+"]"+ " %s \n " % data

        if (data['type'] == 'client'):
            logic_on_client(data)
        elif (data['type'] == 'server'):
            logic_on_server(data)
        else:
            print "type has not been recognised"




def logic_on_client(data):
    device = data['device']
    beacon = data['id_beacon']
    print "device "+device+" beacon "+beacon
    if data['method'] =='post':
        complete_url = url_client_logic+device+"/"+beacon
        print "post on url "+complete_url

        try:
            r = requests.post(complete_url)
            return str(r)
        except requests.exceptions.ConnectionError:
            print "failed to contact server"
            return "failed to contact server"
    elif data['method'] =='delete':
        complete_url =url_client_logic+device
        print "delete on url"+complete_url
        try:
            r = requests.delete(complete_url)
            return str(r)
        except requests.exceptions.ConnectionError:
            print "failed to contact server"
            return "failed to contact server"







def logic_on_server(data):
    if data['method'] == 'post':

        payload =data['data']
        complete_url = url_server_logic+data['device']
        print "post on url "+complete_url+" data "+str(payload)
        try:
            header = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            r = requests.post(complete_url,data=json.dumps(payload), headers=header)
            return str(r)
        except requests.exceptions.ConnectionError:
            print "failed to contact server"
            return "failed to contact server"


    elif data['method'] == 'delete':
        complete_url =url_server_logic+device
        print "delete on url"+complete_url
        try:
            r = requests.delete(complete_url)
            return str(r)
        except requests.exceptions.ConnectionError:
            print "failed to contact server"
            return "failed to contact server"

if __name__ == '__main__':
    runServer()


