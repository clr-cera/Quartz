from threading import Thread
from socket import socket

from ClientLib import clientWire
from Common import serverData, colors

class Client:
    def __init__(self, state: str="ON", channel: int=0):
        self.state: str= state
        self.channel: int= channel
        self.username: str= None
        self.color: str=None
        self.threads: list[Thread]= None
        
        # The socket is automatically connected when Client is innitialized
        self.s: socket = clientWire.connectSocket(serverData.HOST, serverData.PORT)


    def shutdown(self) -> None:
        self.state = "SHUTDOWN"
        exit()
    
    def setUsername(self, name: str) -> None:
        self.username = name
    
    def setColor(self, color: str) -> None:
        if color in colors.COLORS:
            self.color = color
        else:
            print("The color you have chosen is not available")
    
    def CheckState(self) -> None:
        if self.state == "SHUTDOWN":
            exit()