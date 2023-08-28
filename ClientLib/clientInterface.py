from time import sleep
from ClientLib import clientClass, clientWire
from Common import messageLib as mlib

def InterfaceStart(client: clientClass.Client) -> None:
    print("Welcome to ICMChat!")
    sleep(1)

    username = input("Type your username:\n")
    print(f"Your username will be {username}!")
    sleep(1)
    
    print("If you desire to change it later on, you can enter /username [NEW_USERNAME]")
    print("--------------Chat--------------")
    #color = input("Select a Color!")

    client.setUsername(username)
    clientWire.sendCMessage(client.s,mlib.Msg(text=f"/username {client.username}",username=client.username))

def MessageInput(client: clientClass.Client) -> str:
    try:
        return input()
    
    except: 
        client.shutdown()