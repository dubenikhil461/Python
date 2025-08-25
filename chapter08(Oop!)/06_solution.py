class Car:
    def __init__(self,model,brand): #constructor 
        self.model = model #self is context (this in js)
        self.brand = brand
class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = Electric_car("tata","safari","200mh")
isinstance(my_car,Car)
isinstance(my_car,Electric_car)