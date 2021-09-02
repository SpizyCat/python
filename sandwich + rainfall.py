#Sandwich Price
money_in_wallet = 50
sandwich_price = 10
sales_tax = .05 * sandwich_price

sandwich_price += sales_tax
money_in_wallet -= sandwich_price
#print (sandwich_price)


#Rainfall
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall += september_rainfall
annual_rainfall += october_rainfall
annual_rainfall += november_rainfall
annual_rainfall += december_rainfall
print (annual_rainfall)



