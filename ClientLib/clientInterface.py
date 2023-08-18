from time import sleep

class Client:
    def __init__(self, state="ON",channel=0):
        self.state = state
        self.channel = channel
        self.username = None

    def shutdown(self):
        self.state = "SHUTDOWN"
    
    def setUsername(self, name):
        self.username = name

def InterfaceStart():
    print("Welcome to ICMChat!")
    sleep(1)
    username = input("Type your username:\n")
    print(f"Your username will be {username}!")
    sleep(1)
    print("If you desire to change it later on, you can enter /username [NEW_USERNAME]")
    print("--------------Chat--------------")
    #color = input("Select a Color!")
    
    return username

def CheckState(client):
    if client.state == "SHUTDOWN":
        exit()