calories = int(input("How many calories have you eaten today?"))
c = int(3000)
c = c - calories

calhigh = 3000
callow = 0

if c > callow and c < calhigh:   
    print("You can eat", c,"calories today")
elif c < callow:
    print("You have eaten too much today, you will be punished.")
elif c == calhigh:
    print("You haven't eaten anything today, go eat some food.")
else:
    print("You must specify a number")