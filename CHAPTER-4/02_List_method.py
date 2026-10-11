Friends = ["orange", "grapes", "apple", 5, 30.4, False, "rohan"]

# 1. append()
Friends.append("Vivek")
print("After append:", Friends)

# 2. insert()
Friends.insert(2, "banana")
print("After insert:", Friends)

# 3. remove()
Friends.remove("banana")
print("After remove:", Friends)

# 4. pop()
Friends.pop(3)
print("After pop:", Friends)

# 5. index()
print("Index of apple:", Friends.index("apple"))

# 6. count()
print("Count of apple:", Friends.count("apple"))

# 7. reverse()
Friends.reverse()
print("After reverse:", Friends)

# 8. clear()
Friends.clear()
print("After clear:", Friends)