'''f = open("CHAPTER-9/file.txt", "r")
data = f.read()
print(data)
f.close()'''

with open("CHAPTER-9/file.txt", "r") as f:
    print(f.read())