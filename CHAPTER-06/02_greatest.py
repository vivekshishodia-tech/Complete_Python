# find the greatest number

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if (a > b and a > c and a > d):
    print("a is greatest number:", a)

elif (b > a and b > c and b > d):
    print("b is greatest number:", b)

elif (c > a and c > b and c > d):
    print("c is greatest number:", c)

elif (d > a and d > b and d > c):
    print("d is greatest number:", d)
