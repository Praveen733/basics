commands=""
started=False
stopped=False
while True:
    commands=input("> ").lower()
    if commands == "start":
        if started:
            print("car is already started")
        else:
            started=True
            print("Car started ....")
    elif commands == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started=False
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