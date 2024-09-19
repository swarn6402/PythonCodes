class MyCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(MyCar):
    def __init__(self, brand, model, battery_size):
       super().__init__(brand, model)
       self.battery_size = battery_size
    
my_tesla = ElectricCar("Tesla", "Model X", "100kWh")
print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, MyCar))

print(my_tesla.battery_size)
