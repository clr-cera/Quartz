import socket

class Msg:
    def __init__(self, text, sender, username=None):
        self.text = text
        self.sender = sender
        self.username = username


# Create the server socket
def CreateServerSocket(host, port):
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM,0)         
    s.bind((host,port,0,0))

    s.listen(50)       
    s.setblocking(False)

    return s

# Sends the message to all connections
def SendMessage(connections, message, isUserMessage=True):
    if isUserMessage:
        formatedText = f"{message.username}: {message.text}"

    else:
        formatedText = f"Server ~ {message.text}"
    
    print(formatedText)

    for c in connections:
        if c != message.sender:
            c.sendall(str.encode(formatedText))
    

# Receive messages from all connections and checks if any connection has been broken, returns a Msg object with the message and sender, if the connection is broken, the sender is None. If there is no message, returns None
def ReceiveMessage(connections):
    messagesList =[]

    if len(connections) > 0:
        #print(len(connections)) #DEBUG

        for c in connections:
            try:
                message = c.recv(4096)

                if message:
                    messagesList.append(Msg(message.decode(), c))

                else: 
                    messagesList.append(Msg(None,c))
            
            except:
                pass

    return messagesList
        


# Accepts any new connections
def AcceptConnections(connections, s):       # This functions accept a connection and append it to a connection and address lists
    
    try:
        c, addr = s.accept()     # Establish connection with client.
        c.setblocking(False)
        connections.append(c)
        print(f"accepted connection from {c}")
    except:
        pass

# This function closes all connections, the socket of the server and clear connections list
def CloseServer(connections, s): 
    for c in connections:
          c.close()
    s.close()

    connections.clear()
    print("All connections were ended!")