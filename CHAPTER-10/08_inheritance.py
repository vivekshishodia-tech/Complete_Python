class Car:
    @staticmethod
    def start():
        print("car started")

        @staticmethod
        def stop():
            print("car stop")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("fortuner")
car1 = ToyotaCar("prius")

print(car1.start())