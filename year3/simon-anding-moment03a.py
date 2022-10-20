#monthlywage = int(input("Hur mycket tjänar du i månaden?"))#
monthlywage = int(25000)
yearlywage = monthlywage*12
c_tax_rate = 0
l_tax_rate = 0

if yearlywage > 19257:
    c_tax_rate = 0.2136    
    l_tax_rate = 0.1148

c_tax = ((yearlywage - 19257) * c_tax_rate)/12
l_tax = ((yearlywage - 19257) * l_tax_rate)/12
wage_tax = monthlywage - c_tax - l_tax

print("Årslönen är {}".format(round(yearlywage)))
print("Månadslönen är {}kr".format(round(monthlywage)))
print("Kommunalskatten är {}kr".format(round(c_tax)))
print("Landsstingskatten är {}kr".format(round(l_tax)))
print("Kvar efter skatt är {}kr".format(round(wage_tax)))