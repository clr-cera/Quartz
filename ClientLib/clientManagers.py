from ClientLib import clientWire
from ClientLib import clientInterface

# This Manager receives and prints messages
def ReceiveManager(s,client):
    while True:
        clientInterface.CheckState(client)
        clientWire.receiveCMessage(s)

# This Manager receive input from the user and send the message to the server
def SendManager(s,client):
    while True:
        clientInterface.CheckState(client)
        
        message = input()
        possibleCommand = message.lower().split()[0]
        
        if possibleCommand == "/exit":
            client.shutdown()
            continue

        if possibleCommand == "/username":
            client.setUsername(message.split()[1])
        
        if (possibleCommand =="/who") or (possibleCommand == "/whoami"):
            print(f"Your current username is: {client.username}")
            continue
        
        
        clientWire.sendCMessage(s,message)