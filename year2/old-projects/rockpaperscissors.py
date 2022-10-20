import random

choices = ["rock", "paper", "scissors"]
while True:
    inp = input("Rock, paper scissors! ")
    computeranswer = choices[random.randint(0,2)]
    if computeranswer == inp:
        print("You guessed", inp, "and the computer also guessed", computeranswer)
    elif computeranswer == "rock" and inp == "scissors":
        print("You lost, you chose", inp, "and the computer chose", computeranswer)
    elif computeranswer == "scissors" and inp == "paper":
        print("You lost, you chose", inp, "and the computer chose", computeranswer)
    elif computeranswer == "paper" and inp == "rock":
        print("You lost, you chose", inp, "and the computer chose", computeranswer)
    elif computeranswer == "scissors" and inp == "rock":
        print("You won, you chose", inp, "and the computer chose", computeranswer)
    elif computeranswer == "paper" and inp == "scissors":
        print("You won, you chose", inp, "and the computer chose", computeranswer)
    elif computeranswer == "rock" and inp == "paper":
        print("You won, you chose", inp, "and the computer chose", computeranswer)
    else:
        print("Please input a valid choice.")
    playagain = input("Play again y/n ")
    if playagain == "n" or playagain == "no":
        break





