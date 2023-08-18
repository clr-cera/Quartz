from ServerLib import serverWire
from ServerLib import serverCommands


# This Manager accept new connections
def ConnectionsManager(s,connections,usernames):
   while True:
      serverWire.AcceptConnections(connections, s)

# This Manager receives messages and send messages 
def ChatManager(s,connections,usernames):
   while True: 
    message = serverWire.ReceiveMessage(connections)

    if message != None:
        if message.text!=None: # If the connection with someone has ended, this will be evaluated as none
            possibleCommand = message.text.split()[0]
            
            # If the user entered username command, it will try to change the username on the database and if there is no space for that, it will increase the space and then insert the username; If suitable, it will declare all changes in the chat
            if (possibleCommand == "/username") and (len(message.text.split()) > 1):
               serverCommands.changeUsername(connections,usernames,message)    

            else:
               message.username = usernames[connections.index(message.sender)]
               serverWire.SendMessage(connections,message)


        else:
            try:
                message.username = usernames[connections.index(message.sender)]

                usernames.pop(connections.index(message.sender))
                connections.pop(connections.index(message.sender))

                message.text = f"{message.username} has left the chat."
                serverWire.SendMessage(connections,message,isUserMessage=False)
                
            except:
                connections.pop(connections.index(message.sender))