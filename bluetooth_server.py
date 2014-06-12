from model import Beacons,db,Locations
import learning_machine
import bluetooth
import thread
import json
from socket import error as SocketError


name="bt_server"
target_name="siggen"
#uuid="00001101-0000-1000-8000-00805F9B34FB"
uuid="94f39d29-7d6d-437d-973b-fba39e49d4ee"

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

        data = json.loads(myjson)

        print "["+str(address)+"]"+ " %s \n " % data

        if (data['type'] == 'client'):
            logic_on_client(data)
        elif (data['type'] == 'server'):
            logic_on_server(data)
        else:
            print "type has not been recognised"

def test():
    myjson=" {type:'client',method:('post'),data:{device:'device mac',beacon:'beacon id'}}"
    data = json.loads(myjson)
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
        db.session.merge(Locations(device, beacon))
        db.session.commit()
        return
    elif data['method'] =='delete':
        loc =Locations.query.get(device)

        if loc is None:
            print "no location with this characteristic"
            return
        print str(loc)
        db.session.delete(loc)
        db.session.commit()



def logic_on_server(data):
    if data['method'] == 'post':
        print "data "+str(data['data'])

        test_data = []
        info ={}

        for information in data['data']:
            info[information['id_beacon']]=information['distance']
        test_data.append(info)

        prediction = learning_machine.find_best_room(test_data)
        print str(prediction)
        db.session.merge(Locations(data['device'],prediction))
        db.session.commit()

    elif data['method'] == 'delete':
        loc =Locations.query.get(data['device'])
        if loc is None:
            print "no location with this characteristic"
            return
        db.session.delete(loc)
        db.session.commit()


