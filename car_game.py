commands=""
while True:
    commands=input("> ").lower()
    if commands == "start":
        print("Car started ....")
    elif commands == "stop":
        print("Car stopped")
    elif commands =="help":
        print("""
        start-to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif commands == "quit":
        break
    else:
        print("sorry i dont understand")