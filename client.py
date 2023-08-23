from ClientLib import *
from ClientLib.clientManagers import *

from Common import *


def main() -> None:

   # This is an object that will be used to track the clients current state and carry main properties
   client = clientClass.Client()

   # This Starts the Interface
   clientInterface.InterfaceStart(client)

   # These are all necessary parameters for the creation of threads
   managerList = [ReceiveManager, SendManager]
   argumentsList = [client]

   # This creates all necessary threads
   threadsList = threads.ThreadSetup(managerList, argumentsList)
   client.threads = threadsList

   for thread in threadsList:
      thread.join()





if __name__ =="__main__":
   main()