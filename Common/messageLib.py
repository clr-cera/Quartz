import json
from socket import socket

class Msg:
    def __init__(self, text: str, sender: socket, username: str=None):
        self.text = text
        self.sender = sender
        self.username = username

    def encode(self) -> str:
        return json.dumps(self.__dict__, indent=2)
    
    def decode(encodedString: str):
        dict = json.loads(encodedString.decode())
        return Msg(**dict)
    
    def __str__(self) -> str:
            return((f"{self.username}: {self.text}").encode())