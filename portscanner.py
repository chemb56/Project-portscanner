#!/usr/bin/python3
#import module 'socket'
import socket
#create variable 's'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#setup host
host = input("Please enter the ip address:")
#port to scan
port = input("please enter the port you want to scan:")
#Function to perform the actual scan
def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
            print("The port is open")
portScanner(port)