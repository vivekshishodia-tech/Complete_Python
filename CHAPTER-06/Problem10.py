'''Simple Discount Calculator
Take the shopping amount as input and calculate the discount:
- Amount ₹5,000 or above: 20% discount
- Amount ₹3,000 or above: 10% discount
- Amount ₹1,000 or above: 5% discount
- Below ₹1,000: No discount'''



amount = int(input("Enter your shopping amount: "))

if (amount >= 5000):
    discount = (amount * 20 / 100)

elif (amount >= 3000):
    discount = (amount * 10 / 100)

elif (amount >= 1000):
    discount = (amount * 5 / 100)
    
else:
    discount = 0

final_amount = amount - discount

print("Your discount is: ₹", discount)
print("Your final amount is: ₹", final_amount)
