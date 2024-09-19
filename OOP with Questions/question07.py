class MyCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport!"
    
my_new_car = MyCar("Maruti", "800")
print(MyCar.general_description())
print(my_new_car.general_description())