import json
from socket import socket

class Msg:
    def __init__(self, text: str, sender: socket=None, username: str=None, isServer=False):
        self.text: str= text
        self.sender: socket= sender
        self.username: str= username
        self.isServer: bool= False

    def __str__(self) -> str:
        if self.isServer == False:
            return(f"{self.username}: {self.text}")
        else:
            return(f"Server ~ {self.text}")

    def encode(self) -> bytes:
        '''Turns the Msg object into bytes.
            \nWrites bytes as a json string.'''
        return json.dumps(self.__dict__, indent=2).encode()
    
    def decode(encodedString: bytes) -> 'Msg':
        '''Turns bytes into a Msg object.
            \nReads bytes as a json string.'''
        dict = json.loads(encodedString.decode())
        return Msg(**dict)
    

    
    def clearSender(self) -> None:
        '''This clears Msg sender property.'''
        self.sender = None

    def setSender(self, c: socket):
        '''This sets Msg sender property with the passed socket.'''
        self.sender = c
    
    def setServerMessage(self) -> None:
        '''This method configures the message to be sent as a server message.'''
        self.isServer = True
    
    def setText(self,text: str) -> None:
        '''Sets the text to the received parameter.'''
        self.text = text



"""if __name__ == "__main__":
    encodedMessage = Msg(text="/username clara",username="clara").encode()
    decodedMessage = Msg.decode(encodedMessage)
    print(decodedMessage.__dict__)"""