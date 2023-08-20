from ClientLib import clientWire
from ClientLib import clientInterface
from socket import socket
from time import sleep

# This Manager receives and prints messages
def ReceiveManager(s: socket,client: clientInterface.Client) -> None:
    while True:
        sleep(0.05)
        clientInterface.CheckState(client)
        print(clientWire.receiveCMessage(s))

# This Manager receive input from the user and send the message to the server
def SendManager(s: socket,client: clientInterface.Client) -> None:
    while True:
        sleep(0.05)
        clientInterface.CheckState(client)
        
        message = input()
        possibleCommand = message.lower().split()[0]
        
        if possibleCommand == "/exit":
            client.shutdown()
            continue

        elif possibleCommand == "/username":
            client.setUsername(message.split()[1])
        
        elif (possibleCommand =="/who") or (possibleCommand == "/whoami"):
            print(f"Your current username is: {client.username}")
            continue
        
        
        clientWire.sendCMessage(s,message)