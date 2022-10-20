import time
from datetime import datetime

print("Yo, välkommen till tidskonverteraren!")
#Här använder jag en table med en formatterare för att göra något annorlunda och lära mig något nytt istället för att bara printa ut det som vanligt. Det gör det även enklare att formattera texten efter hur jag vill att den ska se ut.
table = {
"Konvertera sekunder till timmar, minuter och sekunder": "s",
"Konvertera timmar och minuter till sekunder": "h",
"Räkna ut differensen mellan två olicka klockslag": "d"}
for statement, letter in table.items():
    print(f"{statement:53s} ==> {letter}")
answer = str(input("Välj en av följande lägen, 's', 'h' eller 'd': "))

if answer == "s":
    sek = int(input("Hej! Skriv ett positivt heltal i sekunder för att omvandla de till timmar, minuter och sekunder: "))
    #ifall de är mer än 86400 sekunder break.
    seks = time.gmtime(sek)
    tid = time.strftime("%H:%M:%S", seks)
    print(tid)

elif answer == "h":
    #en funktion som delar upp input stringen till olika variabler och omvandlar sedan de till sekunder med hjälp av matematik.
    def get_sec(time_str):
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)
    c_time = input("Skriv in en tid i formatet (HH:MM:SS) för att konvertera det till sekunder: ")
    r_time = (get_sec(c_time))
    print("Det blir", r_time, "sekunder") 

elif answer == "d":
    #input för de två olika tiderna.
    start_time = input("Hej, skriv in den första tiden du vill få ut differensen mellan i formatet (HH:MM:SS): ")
    end_time = input("Hej, skriv in den andra tiden du vill få ut differensen mellan i formatet (HH:MM:SS): ")
    #konvertera input stringsen till datetime
    t1 = datetime.strptime(start_time, "%H:%M:%S")
    print('Starttid:', t1.time())
    t2 = datetime.strptime(end_time, "%H:%M:%S")
    print('Sluttid:', t2.time())
    #kalkylering
    delta = t2 - t1
    #printar ut svaret i sekunder.
    print(f"Tidsskillnaden är {delta.total_seconds()} sekunder")

else:
    print("fel input!")
