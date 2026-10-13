# Take a number as input and check whether it is:
# - Divisible by both 5 and 11
# - Divisible only by 5
# - Divisible only by 11
# - Divisible by neither



num = int(input("Enter a number: "))

if (num % 5 == 0 and num % 11 == 0):
    print("Divisible by both 5 and 11")

elif num % 5 == 0:
    print("Divisible only by 5")

elif num % 11 == 0:
    print("Divisible only by 11")

else:
    print("Divisible by neither")
