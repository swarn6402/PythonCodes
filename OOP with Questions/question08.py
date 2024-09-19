class MyCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
    
    @property
    def model(self):
        return self.__model 
    
my_new_car = MyCar("Maruti", "800")
print(my_new_car.model)