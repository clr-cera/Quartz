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
            if client.CheckActions(msg.text, msg.text.lower().split()[0], "receiver", msg) == True:
                continue
            print(str(msg))

# This Manager receive input from the user and send the message to the server
def SendManager(client: clientClass.Client) -> None:
    while True:
        sleep(0.05)
        client.CheckState()

        message = clientInterface.MessageInput(client)
        try:
            possibleCommand = message.lower().split()[0]
        except:
            continue
        
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

        if client.CheckActions(message, possibleCommand,"sender", mlib.Msg(text=message, username=client.username, color=client.color)) == True:
            continue
        
        clientWire.sendCMessage(client.s,mlib.Msg(text=message, username=client.username, color=client.color))
