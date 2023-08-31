import socket
from time import sleep
from Common import messageLib as mlib

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

        

def receiveCMessage(s: socket.socket) -> mlib.Msg:

    try:
        msg: mlib.Msg= mlib.Msg.decode(s.recv(4096))
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
        


        

def sendCMessage(s: socket.socket,msg: mlib.Msg) -> None:
    try:
        s.sendall(msg.encode())
    except:
        print("Connection with host is unstable, trying to send message again...")
        sleep(2)
        sendCMessage(s,msg)
