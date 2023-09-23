# Quartz
Quartz is an extensible tcp chat. It provides a server and a client with more than enough flexibity to suit your use case. It can be deployed in a local network or in the internet with ease due to `nix` integration. To create a Quartz based chat, one can fork this repo and make little changes as described in the Configuration section.

## About
- Authors: clr-cera
- License: MIT License
- Download: https://codeload.github.com/clr-cera/Quartz/zip/refs/heads/main
- Bug reports: https://github.com/clr-cera/Quartz/issues
- git clone https://github.com/clr-cera/Quartz.git
  
## Design Goals
- An easily and completely extensible tcp chat in python
- An easy, fast and integrated deployment using nix
- Console-based but web extensible as well

## Features
- Tcp basic console chat
- Plugin system
- Commands interface
- User selected names and colors

## Dependencies
### Obligatory Dependencies
- `Python` for everything
- `dnspython` for domain resolving
### Optional Dependencies
- `nix` for installation and deployment
- `docker`  for nix produced docker use

## Installing Client
This repo has a Quartz package available inside the flake and also can be installed via `pip`.
### Pip installation: 
```
pip install .
```

### Nix run:
```
nix run github:OWNER/CHAT_REPO
```
This command will "install" everything and run the client automatically.

### In a Nixos flake system:
In flake.nix:
```nix
{
  # create an input with the name of the chat, and set its url to this repository
  inputs.CHATNAME.url = github:OWNER/CHATREPO;
}
```
In configuration.nix:
```nix
{
environment.systemPackages = [inputs.CHATNAME.packages.YOUR_SYSTEM.default];
}
```
## Configuration
### If you want to add plugins to a Quartz based client:
Plugins for client can be inserted in ~/.config/chatname/plugins/.

This folder is automatically created on first client execution.
### If you want to configure a Quartz based chat, you can follow these steps:
0. Step Zero: Fork it, if you are going to make a Quartz based chat please do not send any configuration commit to this repo.
  
1. Firstly: You can find and replace Quartz for whatever name you want inside flake.nix and change the name and console_scripts name inside setup.cfg. Please dont replace the name inside Src!!! (It can break!)
 
2. Secondly: You can enter your information in src/Quartz/__init__.py, such as chat's name, domain, ip, iptype(IPV6 or IPV4) and version. Here, if given IP it will be used, if not, the domain will be converted as IP and if no domain nor IP is given, the host will be localhost.
  
3. Thirdly: You can put every plugin you want inside their respective directories. For Client PLugins: src/Quartz/Clientlib/ClientPlugins. For Server Plugins: src/Quartz/ServerLib/ServerPlugins. Every plugin inserted will be automatically capted by client and Server.

4. Deploy it with your desired method and publish the client!

## Deploy
The server can be deployed in various ways:
- Nix run
```
nix run .#Server
```
This command will install all dependencies and run the server.
- Docker
  
The flake inside this repo makes a docker image available so one can enter:
```
nix build .#Docker
```
In the working directory a `result` docker image with all dependencies will be created. Inside it the `CHATNAME-Server` command can be used to start the server.
- Directly

if one wants, they can just run: 
```
python src/Quartz/server.py
```
Everything should be up and running if all obligatory dependencies are met.

## Plugin Creation
### Client Plugin
Every Client Plugin will be scaned for two functions.
- commands()
The first function is commands(), this is the necessary header of any commands function:
```python
(function) def commands(
client,
message: str,
possibleCommand: str,
role: str,
msgObject: Msg
) -> bool
```
This function receives the client object (See src/Quartz/ClientLib/clientClass.py for client class), a string message, a string possible command, the role(If it is a receiver or the sender of given message) and a Msg object (See src/Quartz/common/messageLib for Msg class). This function is called everytime the client sends or receives a message, if it returns False, the message will continue to be passed to other commands(), and in the end, it will be printed if receiver or sent to server if sender. If a plugin's commands() wants for that message to not be printed or sent, it should return True if given role. See plugin-example for an example of Client Plugin with commands() function.

- manager()
The second function is manager(), this is the necessary header of any manager function:
```python
(function) def manager(
client,
) -> None
```
This function receives the client object (See src/Quartz/ClientLib/clientClass.py for client class). If a plugin has this function, in the client initialization, a thread with this function as a target will be started. The plugin creator will be responsible to all this thread operations and its end, the client has a method CheckState() that can be used to end the thread when the user wants to quit.

### Server Plugin
Every Server Plugin will be scaned for two functions and one list.
- clientCommands()
The first function is clientCommands(), this is the necessary header of any clientCommands function:
```python
(function) def clientCommands(
server,
message: str,
possibleCommand: str,
msgObject: Msg
) -> bool
```
This function receives the server object (See src/Quartz/ServerLib/serverClass.py for server class), a string message, a string possible command and a Msg object (See src/Quartz/common/messageLib for Msg class). This function is called everytime the server receives a message, if it returns False, the message will continue to be passed to other clientCommands(), and in the end, it will be sent to all connections except receiver. If a plugin's clientCommands() wants for that message to not be sent to all connections, it should return True.

- serverCommands()
The second function is serverCommands(), this is the necessary header of any serverCommands function:
```python
(function) def serverCommands(
server,
message: str,
possibleCommand: str,
) -> bool
```
This function receives the server object (See src/Quartz/ServerLib/serverClass.py for server class), a string message and a string possible command. This function is called everytime the server gives an input to the terminal, if it returns False, the message will continue to be passed to other serverCommands().
- MANAGERLIST
The list is MANAGERLIST, this list should contain functions with this header:
```python
(function) def manager(
server,
) -> None
```
All function inside MANAGERLIST are going to be the target of newly created threads on server initialization. The plugin creator will be responsible to all these threads operations.

### Credits
Ranger file manager's README was a heavy inspiration for this file and I am very thankful.
