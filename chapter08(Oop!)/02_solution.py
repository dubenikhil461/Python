class Car:
    def __init__(self,model,brand): #constructor 
        self.model = model #self is context (this is js)
        self.brand = brand
    def fullname(self):
        print(f"{self.model} {self.brand}")
my_car = Car("tata","safari")
print(my_car.fullname())