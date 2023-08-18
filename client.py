from ClientLib import *
from Common import *

# These are all Managers declarations

# This Manager receives and prints messages
def ReceiveManager(s):
    while True:
        clientWire.receiveCMessage(s)

# This Manager receive input from the user and send the message to the server
def SendManager(s):
    while True:
        message = input()
        clientWire.sendCMessage(s,message)

# This creates and connects a socket with server
s = clientWire.connectSocket(serverData.HOST, serverData.PORT)

# This Starts the Interface and sends the chosen username to the server
username = clientInterface.InterfaceStart()
clientWire.sendCMessage(s,f"/username {username}")

# These are all necessary parameters for the creation of threads
managerList = [ReceiveManager, SendManager]
argumentsList = [s]

# This creates all necessary threads
threadsList = threads.ThreadSetup(managerList, argumentsList)
for thread in threadsList:
   thread.join()