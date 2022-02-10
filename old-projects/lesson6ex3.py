n = int(input("Give me a number between 1-12 "))

if n < 10:
    for x in range(0,n*10+n,n): 
        print(x)
elif n > 10:
    n2 = n-10 
    for x in range(0,n*(10+n2)+n,n):
        print(x)