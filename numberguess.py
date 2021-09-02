import random

attempts = 1
secret_number = random.randint(1,100)
guess = int(input("Take a guess: "))

while secret_number != guess and attempts < 6:

    if guess < secret_number:
        print("higher")
    elif guess > secret_number:
        print("lower")
    guess = int(input("Take a guess: "))
    attempts += 1

if attempts == 6:
    print("\nSorry you reached the maximum number of tries")
    print("The secret number was", secret_number)

else:
    print("\nYou guessed the right number! It was ",secret_number)
    print("You guessed it in", attempts,"attempts")

input("\n\n Press the enter key to exit.")
