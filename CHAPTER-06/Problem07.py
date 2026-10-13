'''Take the number of electricity units consumed as input and calculate the bill using these rates:
- First 100 units: ₹5 per unit
- Next 100 units: ₹7 per unit
- Above 200 units: ₹10 per unit'''


units = int(input("Enter the Electricity consumed: "))

if(units < 0):
    print("Invalid units")

elif(units <= 100):
    bill = units * 5
    print("Electricity bill: ₹", bill)

elif(units <= 200):
    bill =(100*5) + ((units-100)*7)
    print("Electricity bill: ₹", bill)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print("Electricity bill: ₹", bill)
    