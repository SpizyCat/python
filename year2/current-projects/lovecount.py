person1 = input("Enter a name to be used for the love meter: ")
person2 = input("Enter a second name to see how compatible they are together: ")

lovecount = 0
 
def heart(x):
   print("""
    LOVE METER:
               ___    ___
              (   \__/   )
               \        /
        >>----- \ {0}% /------>
                 \    /
                  \  /
                   \/
""".format(x))

def lovetester():
    consonants = "qwrtpsdfghjklzxcvbnm"
    vowels = "aeiouy"
    lovecount = 0
    for vowels in person1:
       for vowels in person2:
           if vowels in person1 and vowels in person2:
               lovecount += 2
    for consonants in person1:
       for consonants in person2:
           if consonants in person1 and consonants in person2:
               lovecount + 1
    if len(person1) + len(person2) >= 25:
       lovecount -= lovecount
       print('Error:\n Dont type in surnames or random input')
    if lovecount > 100:
       lovecount = 100
    impossible = (1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97)
    enemies = (2, 10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98)
    shyness = (3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99)
    friends = (4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100)
    slightlove = (5, 13, 21, 29, 37, 45, 53, 61, 69, 77, 85, 93)
    deeplove = (6, 14, 22, 30, 38, 46, 54, 62, 70, 78, 86, 94)
    marriage = (7, 15, 23, 31, 39, 47, 55, 63, 71, 79, 87, 95)
    tilldeath = (8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96)
    if lovecount in impossible:
       print('\t TOTALLY HORRIBLE MATCH!!!')
       print("""
       \tIMPOSSIBLE
     {0} and {1} two will never be together, not even friends\n
     NEVER!!!
     """.format(person1, person2))
       lovecount = -100
    if lovecount in enemies:
       print("""
       \tENEMIES
      With {0} and {1} are enemies. They hate each other.
      """.format(person1, person2))
       lovecount = -5
    if lovecount in shyness:
       print("""
          \tSHYNESS
      {0} and {1} atleast have a chance, but its being hindered by both of them being shy.
      """.format(person1, person2))
       lovecount = 15
    if lovecount in friends:
       print("""
          \tFRIENDS
      {0} and {1} are just friends.
      """.format(person1, person2))
       lovecount = 20
    if lovecount in slightlove:
       print("""
          \tLSlIGHT LOVE
      With {0} and {1} there is a chance this two will fall in love and break up.
      """.format(person1, person2))
       lovecount = 30
    if lovecount in deeplove:
       print("""
          \tDEEP LOVE
      {0} and {1} will probably last long.
      """.format(person1, person2))
       lovecount = 60
    if lovecount in marriage:
       print("""
              \tMARRIAGE
          {0}'s and {1}'s love can end up being really deep. 
          """.format(person1, person2))
 
       lovecount = 80
 
    elif lovecount in tilldeath:
       print("""
              \tTILL DEATH
          {0} and {1} will get married, and live happy life together. 
          """.format(person1, person2))
 
       lovecount = 100
    elif lovecount == 0:
       print("""
              \tUNKNOWN
         It is impossible to determine if {0} and {1} are compatible.
         TOO BAD!
 
     """.format(person1, person2))
 
    heart(lovecount)

lovetester()