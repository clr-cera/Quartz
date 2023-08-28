from ServerLib import serverWire
from ServerLib import serverClass
from time import sleep

# This Manager accept new connections
def ConnectionsManager(server: serverClass.Server) -> None:
   """This function manages all incoming connections from clients and was built to be a thread target"""
   
   while True:
      sleep(0.2)
      
      serverWire.AcceptConnections(server.connections, server.s)

# This Manager receives messages and send messages 
def ChatManager(server: serverClass.Server) -> None:
   """This function manages chat, receiving and sending messages, was built to be a thread target"""

   while True: 
    sleep(0.2)
    messageList = serverWire.ReceiveMessage(server.connections)

    for message in messageList:
        if message != None:
            if message.text!=None: # If the connection with someone has ended, this will be evaluated as none
                possibleCommand = message.text.split()[0]

                # If the user entered username command, it will try to change the username on the database and if there is no space for that, it will increase the space and then insert the username; If suitable, it will declare all changes in the chat
                if (possibleCommand == "/username") and (len(message.text.split()) > 1):
                   server.changeUsername(message)    

                # If there was no command, just send normal message
                else:
                   message.username = server.usernames[server.connections.index(message.sender)]
                   serverWire.SendMessage(server.connections,message)


            else:
                server.removeUser(message)