'''
This Plugin is just an example of a command plugin
'''
import os
from ClientLib.clientClass import Client

def commands(client: Client, message: str, possibleCommand: str):
    if possibleCommand =="/cowsay":
        message.removeprefix(possibleCommand)
        os.system(f"cowsay {message}")