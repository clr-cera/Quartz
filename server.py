from Common import *
from ServerLib import *
import atexit 

def main():

   server = serverClass.Server()

   # These are the lists needed for threads creation
   managerList = [serverManagers.ConnectionsManager, serverManagers.ChatManager]
   argumentsList= [server]

   # This will be executed whenever the server ends
   atexit.register(serverWire.CloseServer,connections=server.connections, s=server.s)

   # Threads creation and join
   threadsList = threads.ThreadSetup(managerList, argumentsList)
   for thread in threadsList:
      thread.join()



if __name__ == '__main__':
   main()