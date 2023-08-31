from threading import Thread
from typing import Callable as Functions, Any

# This functions takes a list of managers, a list of arguments and initializes all managers as separated threads, it returns a list with all threads
def ThreadSetup(managerList: list[Functions], argumentsList: list[Any]) -> list[Thread]:
    threadsList = []
    for manager in managerList:
        t = Thread(target=manager, args=argumentsList, daemon=True)
        t.start()
        threadsList.append(t)
    
    return threadsList