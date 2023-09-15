from ServerLib import serverWire
from socket import socket
from Common import *

class Server:
    def __init__(self) -> None:
        self.connections: list[socket]= []
        self.usernames: list[str]= []
        self.s: socket= serverWire.CreateServerSocket(serverData.HOST, serverData.PORT)

    # This function removes user from connections and usernames lists
    def removeUser(self, message: messageLib.Msg) -> None:

        try:
            userIndex = self.connections.index(message.sender)
            message.username = self.usernames[userIndex]

            self.usernames.pop(userIndex)
            self.connections.pop(userIndex)

            message.text = f"{message.username} has left the chat."
            message.isServer = True
            serverWire.SendServerMessage(self.connections,message)

        except:
            self.connections.pop(userIndex)

    # This function changes or inserts a username in the usernames list
    def changeUsername(self, message: messageLib.Msg) -> None:
        newUsername = message.text.split()[1]

        try:
            oldEntry = self.usernames[self.connections.index(message.sender)]
            self.usernames[self.connections.index(message.sender)] = newUsername

            if oldEntry == None:
                message.text = f"{newUsername} has entered the chat."
                serverWire.SendServerMessage(self.connections,message)

            else:
                message.text = f"{oldEntry} has changed their name to {newUsername}"
                serverWire.SendServerMessage(self.connections,message)
        
        

        except:
            difference = self.connections.index(message.sender)+1 - len(self.usernames)
            self.usernames.extend([None]*difference)

            self.usernames[self.connections.index(message.sender)] = newUsername

            message.username = newUsername
            message.text = f"{message.username} has entered the chat."

            serverWire.SendServerMessage(self.connections,message)
