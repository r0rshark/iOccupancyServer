import bluetooth
import thread
import json
import requests
from socket import error as SocketError


name="bt_server"
target_name="siggen"
#uuid="00001101-0000-1000-8000-00805F9B34FB"
uuid="94f39d29-7d6d-437d-973b-fba39e49d4ee"
url_client_logic="http://127.0.0.1/ibeacon/"
url_server_logic="http://127.0.0.1/ibeaconserver/"

def runServer():
    serverSocket=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
    port=bluetooth.PORT_ANY
    serverSocket.bind(("",port))
    print "Listening for connections on port: ", port
    serverSocket.listen(2)
    port=serverSocket.getsockname()[1]

    #the missing piece
    bluetooth.advertise_service( serverSocket, "SampleServer",service_id = uuid,service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ], profiles = [ bluetooth.SERIAL_PORT_PROFILE ])


    while True:
        print "waiting connection"
        inputSocket, address=serverSocket.accept()
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

       try :
            r = requests.post(complete_url)
            return str(r)
        except ConnectionError:
            print "failed to conctact server"
            return "failed to conctact server"
    elif data['method'] =='delete':
        complete_url =url_client_logic+device
        print "delete on url"+complete_url
        try:
            r = requests.delete(complete_url)
            return str(r)
        except ConnectionError:
            print "failed to conctact server"
            return "failed to conctact server"







def logic_on_server(data):
    if data['method'] == 'post':

        payload =data['data']
        complete_url = url_server_logic+data['device']
        print "post on url "+complete_url+" data "+str(payload)
        try:
            r = requests.post(complete_url,params=payload)
            return str(r)
        except ConnectionError:
            print "failed to conctact server"
            return "failed to conctact server"


    elif data['method'] == 'delete':
        complete_url =url_server_logic+device
        print "delete on url"+complete_url
        try:
            r = requests.delete(complete_url)
            return str(r)
        except ConnectionError:
            print "failed to conctact server"
            return "failed to conctact server"

runServer()
