while True:
    menu = int(input(
        "Hello, welcome to Simon's music menu!\nChoose a genre:\n1. Rap\n2. Rock\n3. Shoegaze\n4. Pop\n5. Exit\n"))
    if menu == 1:
        print("You will now listen to Rap.")
    elif menu == 2:
        print("You will not listen to Rock")
    elif menu == 3:
        print("You will not listen to Shoegaze")
    elif menu == 4:
        print("You will not listen to Pop")
    elif menu == 5:
        print("Goodbye.")
    else:
        print("Please specify a number between 1-4")
    playagain = input("Listen to another song, y/n ")
    if playagain == "n" or playagain == "no":
        break
