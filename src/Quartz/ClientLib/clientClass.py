from threading import Thread
from socket import socket

from ClientLib import clientWire
from Common import serverData, colors

from types import ModuleType
import importlib
import pkgutil
from ClientLib import ClientPlugins
from Common.messageLib import Msg


def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

discovered_plugins = [
    importlib.import_module(name)
    for finder, name, ispkg
    in iter_namespace(ClientPlugins)
]

class Client:
    def __init__(self, state: str="ON", channel: int=0):
        self.state: str= state
        self.channel: int= channel
        self.username: str= None
        self.color: str=None
        self.threads: list[Thread]= None
        self.plugins: dict[ModuleType]= discovered_plugins
        
        # The socket is automatically connected when Client is innitialized
        self.s: socket = clientWire.connectSocket(serverData.HOST, serverData.PORT)


    def shutdown(self) -> None:
        self.state = "SHUTDOWN"
        exit()
    
    def setUsername(self, name: str) -> None:
        self.username = name
    
    def setColor(self, color: str) -> None:
        if color in colors.COLORS:
            self.color = color
        else:
            print("The color you have chosen is not available")
    
    def CheckState(self) -> None:
        if self.state == "SHUTDOWN":
            exit()

    def CheckActions(self, message: str, possibleCommand: str, role: str, msgObject: Msg) ->None:
        '''This Function iterates on all plugins searching for commands to check, role can be "sender" or "receiver", which will be defined by the manager'''
        for plugin in self.plugins:
            try:
                if plugin.commands(self, message, possibleCommand, role, msgObject) == True:
                    return True
            except:
                pass
        return False