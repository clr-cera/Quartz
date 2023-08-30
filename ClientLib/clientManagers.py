from ClientLib import *
from socket import socket
from time import sleep
from Common import messageLib as mlib

# This Manager receives and prints messages
def ReceiveManager(client: clientClass.Client) -> None:
    while True:
        sleep(0.05)
        client.CheckState()

        msg = clientWire.receiveCMessage(client.s)
        if msg != None:
            print(str(msg))

# This Manager receive input from the user and send the message to the server
def SendManager(client: clientClass.Client) -> None:
    while True:
        sleep(0.05)
        client.CheckState()

        message = clientInterface.MessageInput(client)

        possibleCommand = message.lower().split()[0]
        
        if possibleCommand == "/exit":
            client.shutdown()
            continue

        elif possibleCommand == "/username":
            client.setUsername(name:=message.split()[1])
            print(f"Now you username is {name}")
        
        elif possibleCommand == "/color":
            clientInterface.ReceiveColor(client)
            continue
        
        elif (possibleCommand =="/who") or (possibleCommand == "/whoami"):
            print(f"Your current username is: {client.username}")
            continue
        
        
        clientWire.sendCMessage(client.s,mlib.Msg(text=message, username=client.username, color=client.color))
