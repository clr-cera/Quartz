from time import sleep
from ClientLib import clientClass, clientWire
from Common import messageLib as mlib

def InterfaceStart(client: clientClass.Client) -> None:
    print("Welcome to ICMChat!")
    sleep(1)

    username = input("Type your username:\n")
    print(f"Your username will be {username}!")
    sleep(1)
    print("If you desire to change it later on, you can enter /username USERNAME")
    
    color = input("Select a Color!")
    print(f"Your color will be {color}!")
    print("If you desire to change it later on, you can enter /color COLOR")
    print("--------------Chat--------------")

    client.setUsername(username)
    client.setColor(color)
    clientWire.sendCMessage(client.s,mlib.Msg(text=f"/username {client.username}",username=client.username))

def MessageInput(client: clientClass.Client) -> str:
    try:
        return input()
    
    except: 
        client.shutdown()
