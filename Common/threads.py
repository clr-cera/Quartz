import threading

def ThreadSetup(managerList, argumentsList):
    threadsList = []
    for manager in managerList:
        t = threading.Thread(target=manager, args=argumentsList, daemon=True)
        t.start()
        threadsList.append(t)
    
    return threadsList