from ServerLib import serverWire
from ServerLib import serverActions
from time import sleep
from socket import socket

# This Manager accept new connections
def ConnectionsManager(s: socket,connections: list[socket],usernames: list[str]) -> None:
   while True:
      sleep(0.2)
      
      serverWire.AcceptConnections(connections, s)

# This Manager receives messages and send messages 
def ChatManager(s: socket,connections: list[socket],usernames: list[str]) -> None:
   while True: 
    sleep(0.2)

    messageList = serverWire.ReceiveMessage(connections)

    for message in messageList:
        if message != None:
            if message.text!=None: # If the connection with someone has ended, this will be evaluated as none
                possibleCommand = message.text.split()[0]

                # If the user entered username command, it will try to change the username on the database and if there is no space for that, it will increase the space and then insert the username; If suitable, it will declare all changes in the chat
                if (possibleCommand == "/username") and (len(message.text.split()) > 1):
                   serverActions.changeUsername(connections,usernames,message)    

                # If there was no command, just send normal message
                else:
                   message.username = usernames[connections.index(message.sender)]
                   serverWire.SendMessage(connections,message)


            else:
                serverActions.removeUser(connections,usernames,message)