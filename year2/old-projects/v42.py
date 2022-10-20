money_in_wallet = 40
sandwich_price = 7.50
baguette_price = 10
coffe_price = 5

while True:
    print("\nWelcome to my cafe menu!", "\n1. Sandwich: 7.5$", "\n2. Baguette: 10 $", "\n3. Coffe: 5$")
    product = int(input("\nPlease choose a product from the menu "))
    if product == 1:
        tax = sandwich_price * .08
        sandwich_price = sandwich_price + tax
        print("Your total will be,", sandwich_price, "You now have", money_in_wallet - sandwich_price, "dollars in your bank account.")

    elif product == 2:
        tax = baguette_price * .08
        baguette_price = baguette_price + tax
        print("Your total will be,", baguette_price, "You now have", money_in_wallet - baguette_price, "dollars in your bank account.")

    elif product == 3:
        tax = coffe_price * .08
        coffe_price = coffe_price + tax
        print("Your total will be,", coffe_price, "You now have", money_in_wallet - coffe_price, "dollars in your bank account.")

    else:
        print("You did not specify a correct input")
    again = input("Do you want to order another item? y/n")
    if again == "n" or again == "no":
        break

