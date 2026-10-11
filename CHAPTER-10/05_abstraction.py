# Abstraction - Hiding implementation details and showing only essential features.

class Car:
    def __init__(self):
        self.acceleration = "false"
        self.brake = "false"
        self.clutch = "false"

    def start(self):
        self.acceleration = "true"
        self.brake = "true"
        print("Car started...")


car1 = Car()
car1.start()
