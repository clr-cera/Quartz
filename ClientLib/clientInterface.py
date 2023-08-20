from time import sleep
from threading import Thread

class Client:
    def __init__(self, state: str="ON", channel: int=0):
        self.state = state
        self.channel = channel
        self.username = None
        self.threads: list[Thread] = None

    def shutdown(self) -> None:
        self.state = "SHUTDOWN"
    
    def setUsername(self, name: str) -> None:
        self.username = name

def InterfaceStart() -> None:
    print("Welcome to ICMChat!")
    sleep(1)

    username = input("Type your username:\n")
    print(f"Your username will be {username}!")
    sleep(1)
    
    print("If you desire to change it later on, you can enter /username [NEW_USERNAME]")
    print("--------------Chat--------------")
    #color = input("Select a Color!")
    
    return username

def CheckState(client: Client) -> None:
    if client.state == "SHUTDOWN":
        exit()