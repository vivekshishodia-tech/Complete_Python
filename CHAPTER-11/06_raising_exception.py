a = int(input("Hey, enter the number: "))
b = int(input("Hey, enter the second number: "))


if (b == 0):
    raise ZeroDivisionError("Hey, our program is not meant to divide number by zero")
else:
    print(f"the division a/b is{a/b}")
