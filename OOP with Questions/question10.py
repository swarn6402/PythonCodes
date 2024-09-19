class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return "this is the battery"

class Engine:
    def engine_info(self):
        return "this is the engine"

class ElectricCar(Car, Battery, Engine):
    pass

my_tesla = ElectricCar("Tesla", "Model S")
print(my_tesla.model)
print(my_tesla.battery_info())
print(my_tesla.engine_info())