from time import sleep
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