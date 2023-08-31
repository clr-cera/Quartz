from time import sleep
from ClientLib import clientClass, clientWire
from Common import messageLib as mlib, colors

def InterfaceStart(client: clientClass.Client) -> None:
    print("Welcome to ICMChat!")
    sleep(1)

    ReceiveUsername(client)
    ReceiveColor(client)

    print("--------------Chat--------------")


    clientWire.sendCMessage(client.s,mlib.Msg(text=f"/username {client.username}",username=client.username))

def MessageInput(client: clientClass.Client) -> str:
    try:
        return input()
    
    except: 
        client.shutdown()


def ReceiveUsername(client: clientClass.Client) -> None:
    username = input("Type your username:\n")
    print(f"Your username will be {username}!")
    client.setUsername(username)
    sleep(1)
    print("If you desire to change it later on, you can enter /username USERNAME")

def ReceiveColor(client: clientClass.Client) -> None:
    while(True):
        color = input(f"""Select a Color!
{colors.COLORS['red']}red 
{colors.COLORS['green']}green 
{colors.COLORS['yellow']}yellow 
{colors.COLORS['lightPurple']}lightPurple 
{colors.COLORS['purple']}purple 
{colors.COLORS['cyan']}cyan 
{colors.COLORS['lightGray']}lightGray 
{colors.COLORS['black']}black
{colors.RESETCOLOR}""")
        
        if color in colors.COLORS:
            print(f"Your color will be {color}!")
            client.setColor(color)
            break

        else:
            print("Your selected color is not available!")

    sleep(1)
    print("If you desire to change it later on, you can enter /color")