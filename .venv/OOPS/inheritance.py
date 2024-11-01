class Car:
    color = "black"

    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def _init__(self, name):
        self.name = name

car1 = ToyotaCar()
car2 = ToyotaCar()

print(car1.start())
print(car1.color)


