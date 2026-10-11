''' write a program tp print pattern
*
**
***
'''
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print("*"*i, end="")
    print(" ")