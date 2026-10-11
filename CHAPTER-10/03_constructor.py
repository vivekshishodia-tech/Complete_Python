class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("Adding new student in database...")


s1 = Student("Rohan")
print(s1.name)


