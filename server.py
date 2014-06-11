import bluetooth
import thread

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
    try:
        while True:
	data=inputSocket.recv(1024)
	if not data:
	  break
	print "["+str(address)"]"+ " %s \n " % data
    except SocketError as e:
        print "client "+str(address)+" has disconnected"
        inputSocket.close()
        time.sleep(0,001)



runServer()
