import json

class Msg:
    def __init__(self, text, sender, username=None):
        self.text = text
        self.sender = sender
        self.username = username

    def encode(self):
        return json.dumps(self.__dict__, indent=2)
    
    def decode(string):
        dict = json.loads(string)
        return Msg(**dict)
    
    def __str__(self) -> str:
            return(f"{self.username}: {self.text}")