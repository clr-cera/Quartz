from Common import *
from ServerLib import *
import atexit 



# These lines declares all main variables for the managers 
connections = [] 
usernames =[]

s = serverWire.CreateServerSocket(serverData.HOST, serverData.PORT)

# These are the lists needed for threads creation
managerList = [serverManagers.ConnectionsManager, serverManagers.ChatManager]
argumentsList= [s,connections,usernames]

# This will be executed whenever the server ends
atexit.register(serverWire.CloseServer,connections=connections, s=s)

# Threads creation and join
threadsList = threads.ThreadSetup(managerList, argumentsList)
for thread in threadsList:
   thread.join()