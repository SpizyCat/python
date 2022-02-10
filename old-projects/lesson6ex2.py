while True:
    print("Welcome to my calculator, give me two numbers and then choose between different mathematical actions.")
    number1 = int(input("Give me a number "))
    number2 = int(input("Give me another number "))

    action = int(input("Which mathematical action do you want to be performed, Choose:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Find the power of\n"))

    if action == 1:
        print(number1, "+", number2, "=",number1 + number2)
    elif action == 2:
        print(number1, "-", number2, "=", number1 - number2)
    elif action ==3:
        print(number1, "*",number2, "=", number1 * number2)
    elif action ==4:
        print(number1, "/",number2, "=", number1 / number2)
    elif action ==5:
        print(number1, "^",number2, "=", number1 ** number2)
    else:
        print("Please specify a correct choice.")
    again = input("Do you want to calculate something else? y/n ")
    if again in ["n", "no"]: 
        break