import socket               # Import socket module
from time import sleep

def connectSocket(host, port):
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)          # Create a socket object
        s.connect((host, port,0,0))
        return s
    except:
        print("The host could not be reached")
        sleep(3)
        print("Trying again!")
        sleep(5)
        return connectSocket(host,port)

        

def receiveCMessage(s):
    try:
        msg = s.recv(4096).decode()
        if msg:
            print(f"{msg}")

    except:
        print("CONNECTION WITH HOST WAS INTERRUPTED!")
        sleep(1)
        print("RESTORING CONNECTION")
        sleep(3)
        receiveCMessage(s)
        
        

def sendCMessage(s,msg):
    try:
        s.sendall(str.encode(msg))
    except:
        print("Connection with host is unstable, trying to send message again...")
        sleep(2)
        sendCMessage(s,msg)