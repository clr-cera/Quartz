from ClientLib import *
from Common import *

# These are all Managers declarations

# This creates and connects a socket with server
s = clientWire.connectSocket(serverData.HOST, serverData.PORT)

# This is an object that will be used to track the clients current state
client = clientInterface.Client()

# This Starts the Interface and sends the chosen username to the server
username = clientInterface.InterfaceStart()
client.setUsername(username)

clientWire.sendCMessage(s,f"/username {client.username}")

# These are all necessary parameters for the creation of threads
managerList = [clientManagers.ReceiveManager,clientManagers.SendManager]
argumentsList = [s,client]

# This creates all necessary threads
threadsList = threads.ThreadSetup(managerList, argumentsList)
for thread in threadsList:
   thread.join()