class MyCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def CarDisplay(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(MyCar):
    def __init__(self, brand, model, battery_size):
       super().__init__(brand, model)
       self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    
my_new_car = MyCar("Maruti", "Ertiga")
print(my_new_car.fuel_type())

my_electric_car = ElectricCar("Tesla", "Model X", "100 kWh")
print(my_electric_car.fuel_type())