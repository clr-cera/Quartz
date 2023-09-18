'''
This Plugin is just an example of a command plugin, as this is a client plugin, it should be placed at ClientLib/ClientPlugins
'''
import os
from Common.messageLib import Msg

def commands(client, message: str, possibleCommand: str, role: str, msgObject: Msg):
    if possibleCommand =="/cowsay":
        message = str(message.split(' ', 1)[1])
        print(role)
        print(str(msgObject))
        os.system(f"cowsay {message}")
        
        if role == "receiver":
            return True
        else:
            return False