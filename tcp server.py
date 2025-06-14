#!/usr/bin/python3
#import socket function
import socket

#Create socket object and specify socket family, type
serversocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

#Create object to store hostnames
host = socket.gethostname ()

#specify the port to listen on
port = 444

#Bind the values to a new oobject server socket
serversocket.bind ((host, port))

#Listen for TCP connection
serversocket.listen[3]

#while loop for connection

while True:
     clientsocket, address = serversocket.accept ()


     print ("received connection from" % str (address))

     message = "Hello and thank you for connecting to the server" + "\r\n"
     clientsocket.send (message)
     #encode message
     clientsocket.send(message.encode["ascii"])
     
     #close the client socket we created
     clientsocket.close()