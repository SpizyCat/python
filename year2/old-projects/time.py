from datetime import date
from dateutil.relativedelta import relativedelta

print("A simple program to calculate your age\n")

birth_str = input('Enter the date you were born, in format YYYY-MM-DD: ')
try:
    birth = date.fromisoformat(birth_str)
except ValueError:
    print("Don't you know your birthday?")
    exit()

age = relativedelta(date.today(), birth)
print(f'You are {age.years} years, {age.months} months and {age.days} days old.')