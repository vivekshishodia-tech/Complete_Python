# write the program to greet all the person names stored in a list 'l' and which start with 's' 

l = ["Subham", "Amit", "Rohan", "Sahil", "Sumit", "Vivek"]

for name in l:
    if name.startswith("S"):
        print("Hello", name)