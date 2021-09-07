number = int(input("Give me a number "))
remainder = number % 2

is_divisble = remainder == 0

if is_divisble == 0: 
    print("You have given me an odd number.")
else:
    print("You have given me an even number")