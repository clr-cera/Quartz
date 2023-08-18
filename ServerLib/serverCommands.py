from ServerLib import serverWire

def changeUsername(connections,usernames,message):
    username = message.text.split()[1]

    try:
        oldEntry = connections.index(message.sender)
        usernames[connections.index(message.sender)] = username

        if oldEntry == None:
            message.text = f"{username} has entered the chat."
            serverWire.SendMessage(connections,message,isUserMessage=False)

        else:
            message.text = f"{oldEntry} has changed their name to {username}"
            serverWire.SendMessage(connections,message,isUserMessage=False)
    
    

    except:
        difference = connections.index(message.sender)+1 - len(usernames)
        usernames.extend([None]*difference)

        usernames[connections.index(message.sender)] = username

        message.username = username
        message.text = f"{message.username} has entered the chat."
        serverWire.SendMessage(connections,message,isUserMessage=False)