number = int(input("Give me a number "))
check = int(input("Give a number to divide by "))
remainder = number % 2
remainder4 = number % 4

is_divisble = remainder == 0
is_divisble4 = remainder4 == 0

if number % 2 == 0: 
    print("You have given me an even number")
else:
    print("You have given me an odd number.")

if is_divisble4 == 0:
    print("You have given me a multiple of a number which isn't a multiple of four.")
else:
    print("You have given me a multiple of four.")

if number % check == 0:
    print(number, "divides evenly by", check)
else:
    print(number, "does not divide evenly by", check)
