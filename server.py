import bluetooth

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
    
    inputSocket, address=serverSocket.accept()
    print "Got connection with" , address
    while True:
	data=inputSocket.recv(1024)
	if not data:
	  break    
	print "received [%s] \n " % data    
    inputSocket.close()
    time.sleep(0,001)
    
    serverSocket.close()  

runServer()
