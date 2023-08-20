from ServerLib import serverWire
from Common import messageLib
from socket import socket

# This function changes or inserts a username in the usernames list
def changeUsername(connections: list[socket], usernames: list[str], message: messageLib.Msg) -> None:
    username = message.text.split()[1]

    try:
        oldEntry = usernames[connections.index(message.sender)]
        usernames[connections.index(message.sender)] = username

        if oldEntry == None:
            message.text = f"{username} has entered the chat."
            serverWire.SendMessage(connections,message,isUserMessage=False)

        else:
            message.text = f"{oldEntry} has changed their name to {username}"
            serverWire.SendMessage(connections,message,isUserMessage=False)
    
    

    except:
        difference = connections.index(message.sender)+1 - len(usernames)
        usernames.extend([None]*difference)

        usernames[connections.index(message.sender)] = username

        message.username = username
        message.text = f"{message.username} has entered the chat."
        serverWire.SendMessage(connections,message,isUserMessage=False)

# This function removes user from connections and usernames lists
def removeUser(connections: list[socket], usernames: list[str], message: messageLib.Msg) -> None:
    
    try:
        message.username = usernames[connections.index(message.sender)]

        usernames.pop(connections.index(message.sender))
        connections.pop(connections.index(message.sender))

        message.text = f"{message.username} has left the chat."
        serverWire.SendMessage(connections,message,isUserMessage=False)

    except:
        connections.pop(connections.index(message.sender))