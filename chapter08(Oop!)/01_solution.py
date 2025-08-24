class Car:
    def __init__(self,model,brand): #constructor 
        self.model = model #self is context (this is js)
        self.brand = brand
    
my_car = Car("tata","safari")
print(my_car.brand)
print(my_car.model)