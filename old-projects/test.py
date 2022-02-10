while True:
    print("Welcome to Simons calculator")
    action = int(input("Choose what you want to do; 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Power of: "))
    number1 = int(input("Give me a number to calculate with. "))
    if action == 1:
        number2 = int(input("Give me another number to add to"))
        print(number1, "+", number2, "=", number1+number2)
        number3 = number1+number2

    elif action == 2:
        number2 = int(input("Give me another number to subtract the first one with."))
        print(number1, "-", number2, "=", number1-number2)
        number3 = number1-number2

    elif action ==3:
        number2 = int(input("Give me another number to multiply the first one with."))
        print(number1, "X", number2, "=", number1*number2)
        number3 = number1*number2

    elif action ==4: 
        number2 = int(input("Give me another number to divise the first one with"))
        print(number1, "/", number2, "=", number1/number2)
        number3 = number1/number2

    elif action ==5:
        number2 = int(input("Give me another number for the power of the first one"))
        print(number1, "^", number2, "=", number1**number2)
        number3 = number1**number2
    
    again = input("Do you want to continue, restart or exit? C / R / E")
    if again in ("E"):
        break
    elif again in ("R"): 
        action2 = int(input("Choose what you want to do with your result; 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Power of: "))
        if action2 == 1:
            number4 = int(input("Give me another number to add to the first one"))
            print(number3, "+", number4, "=", number3+number4)

        elif action == 2:
            number4 = int(input("Give me another number to subtract the first one with."))
            print(number3, "-", number4, "=", number3-number4)

        elif action ==3:
            number4 = int(input("Give me another number to multiply the first one with."))
            print(number3, "X", number4, "=", number3*number4)

        elif action ==4: 
            number4 = int(input("Give me another number to divise the first one with"))
            print(number3, "/", number4, "=", number3/number4)

        elif action ==5:
            number4 = int(input("Give me another number for the power of the first one"))
            print(number3, "^", number4, "=", number3**number4)
    restart = input("Do you want to restart or exit? R / E")
    if again in ("E"):
        break