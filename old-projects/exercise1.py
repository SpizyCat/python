from datetime import date
todays_date = date.today()

name = input("What is your name? ")
age = int(input("How old are you? "))

year100 = todays_date.year - age + 100

if age == 100 or age > 100:
    print("You have already turned a 100 years old.")

else:
    print(name, "will turn 100 years old in", year100)

number = int(input("Give me a number! "))
for i in range(number):
    print(name, "will turn 100 years old in", year100)