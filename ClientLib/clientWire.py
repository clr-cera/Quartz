import socket
from time import sleep

def connectSocket(host: str, port: int) -> socket.socket:
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        s.connect((host, port,0,0))
        s.setblocking(False)
        return s
    
    except:
        print("The host could not be reached")
        sleep(3)
        print("Trying again!")
        sleep(5)
        return connectSocket(host,port)

        

def receiveCMessage(s: socket.socket) -> None:

    try:
        msg = s.recv(4096).decode()
        if msg:
            return msg

        else:
            print("CONNECTION WITH HOST WAS INTERRUPTED!")
            sleep(1)
            print("RESTORING CONNECTION")
            sleep(3)
            receiveCMessage(s) 
    
    except:
        pass
        


        

def sendCMessage(s: socket.socket,msg: str) -> None:
    try:
        s.sendall(str.encode(msg))
    except:
        print("Connection with host is unstable, trying to send message again...")
        sleep(2)
        sendCMessage(s,msg)
