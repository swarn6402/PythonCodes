class MyCar:
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model

my_car = MyCar("Maruti", "800")
print(my_car.brand)
print(my_car.model)

my_other_car = MyCar("MarutiSuzuki", "Ertiga")
print(my_other_car.model)