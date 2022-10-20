while True:
    pw = input("Tell me your password ")
    if len(pw) >= 8:
        print("You have given me a password.")
        print("The first letter you gave me was", pw[0].upper())
        break
    elif len(pw) <= 8:
        print("Your password needs to be atleast 8 characters long.")