word = []
word = input("Give me a word ")

def ispalindrome(s):
    return s == s[::-1]

s = word
ans = ispalindrome(s)

if ans:
    print("Yes")
else:
    print("No")