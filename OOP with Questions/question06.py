class MyCar:
    
    Number_of_Cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        MyCar.Number_of_Cars += 1 

my_car = MyCar("Maruti", "800")
my_other_car = MyCar("MarutiSuzuki", "Ertiga")


print(MyCar.Number_of_Cars)    