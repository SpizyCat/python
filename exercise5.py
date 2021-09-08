import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set(a).intersection(b))

randomlist1 = random.sample(range(0,15), 7)
randomlist2 = random.sample(range(0,15), 7)
print(randomlist1, randomlist2)
print(set(randomlist1).intersection(randomlist2))

print(set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]).intersection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))