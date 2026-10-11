student = {
    "name": "Vivek",
    "age": 20,
    "course": "B.Tech"
}

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# get()
print(student.get("name"))

# update()
student.update({"marks": 80})
print(student)

# pop()
student.pop("age")
print(student)

# clear()
student.clear()
print(student)