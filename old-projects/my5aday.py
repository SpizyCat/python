print("Welcome to My5aDay.")
my5aday = int(input("How many vegetables or fruit have you eaten today?"))

#fav = fruit and veggies
fav = int(5)
fav = fav - my5aday

favlow = 0
favhigh = 5

if fav == 5:
    print("You haven't eaten any fruits or veggies today! EAT SOME NOW.")

elif fav > favlow and fav < favhigh:
    print("You have to eat", fav,"more fruit or veggies, good job but not done!")

elif fav == favlow or fav < favlow:
    print("You have eaten enough fruit and veggies today! You can always eat a few more because they are so tasty!")