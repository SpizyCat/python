import math
#Allting är rätt simpelt och inget är nytt, känner därför inte behovet av att kommentera ut något.

answer1 = input("Vill du använda ett decimaltal för att beskriva radien? Skriv nej för att istället använda heltal: ")
answer1 = answer1[0]
answer1 = answer1.upper()

if answer1 == "J":
    radie = float(input("Vad är radien? (i decimaltal)"))
    area = math.pi * radie ** 2
    area = round(area, 2)
    omkrets = math.pi * 2 * radie
    omkrets = round(omkrets, 2)
elif answer1 == "N":
    radie = int(input("Vad är radien? (i heltal)"))
    area = math.pi * radie ** 2
    area = round(area, 2)
    omkrets = math.pi * 2 * radie
    omkrets = round(omkrets, 2)
print("Radien är ", radie, "cm, arean är ", area, "cm\u00b2 och omkretsen är ", omkrets, "cm")
