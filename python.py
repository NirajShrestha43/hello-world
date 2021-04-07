command = ""
started = True
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = False
            print("car started..")
    elif command == "stop":
        print("car has stopped")
    elif command == "help":
        print("""start - to start the car
stop - to stop the car
help - to open menue""")
    elif command == "quit":
        break
else:
        print("i don't understand that...")