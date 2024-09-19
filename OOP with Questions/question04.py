class MyCar:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"
    
    
my_new_car = MyCar("Tesla", "Model X")
print(my_new_car.get_brand())
