class MyCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def CarDisplay(self):
        return f"{self.brand} {self.model}"

my_new_car = MyCar("Maruti Suzuki", "800")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.CarDisplay())

my_other_car = MyCar("Maruti", "Ertiga")
print(my_other_car.CarDisplay())