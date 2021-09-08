number = int(input("Give me a number "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a2 = [i for i in a if i <= 4]
a3 = []
a3.append(a2)

mylist = [i for i in a if i <= number]
print(mylist)

