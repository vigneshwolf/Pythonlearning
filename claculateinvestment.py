#We are going to calculate investment.
amount = float(input("Enter amount: "))
inrate = float(input("Enter intrest rate: "))
period = int(input("Enter Year: "))
value = 0 
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year %d Rs. %2f" % (year , value))
    amount = value
    year = year + 1
               
