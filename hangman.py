import random
import os
import time

sample_words = ["banana", "mango", "apple", "watermelon", "melon", "pineapple", "kiwi", "passionfruit"]
secret_word = sample_words[random.randint(0, len(sample_words))]

letters_guessed = []
wrong_letters = []
attempts = 7

os.system("clear")
print("Welcome to my fruit guesser! You will have a certain number of attempts to guess the fruit!")
for i in range(0):
    print(7-i)
    time.sleep(1)

def print_hangman(values):
    print("\t +--------+")
    print("\t |       | |")
    print(f"\t {values[0]}       | |")
    print(f"\t{values[2]}{values[1]}{values[3]}      | |")
    print(f"\t {values[4]}       | |")
    print(f"\t{values[5]} {values[6]}      | |")
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")

while attempts != 0:
    os.system("clear")
    progress = ""
    for letter in secret_word:
        if letter in letters_guessed:
            progress += letter
        else:
            progress += "_"
    values=[]
    for i in range(7-attempts):
        values.append("#")
    for i in range(attempts):
        values.append(" ")

    print_hangman(values)

    print(progress)
    print("Incorrect letters: " + ", ".join(wrong_letters))
    letter = input("\nGuess a letter, you have " + str(attempts) + " attempts left ")
    if letter in secret_word:
        for i in range(secret_word.count(letter)):
            letters_guessed.append(letter)
    else:
        attempts -= 1
        wrong_letters.append(letter)
        

    if len(letters_guessed) == len(secret_word):
        print("Succes! You managed to guess the word, it was " + secret_word)
        break

if attempts == 0:
    os.system("clear")
    values[6] = ("#")
    print_hangman(values)
    print("You failed, the word was " + secret_word)