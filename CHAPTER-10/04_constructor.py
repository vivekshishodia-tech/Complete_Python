class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Adding new student in database...")


s1 = Student("Rohan", 88)
print(s1.name, s1.marks)

s2 = Student("Vivek", 91)
print(s2.name, s2.marks)
