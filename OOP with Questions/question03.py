class MyCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def CarDisplay(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(MyCar):
    def __init__(self, brand, model, battery_size):
       super().__init__(brand, model)
       self.battery_size = battery_size
    
my_electric_car = ElectricCar("Tesla", "Model X", "100kWh")
print(my_electric_car.battery_size)
print(my_electric_car.CarDisplay())