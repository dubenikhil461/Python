class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    @staticmethod #decorator
    def car_info(): #no need of self
        print("This is a static method of Car class.")

    def func(self):
        print(f"{self.brand}{self.model}")
    
    @property
    def modelChange(self):
        return self.model

my_car = Car("tata","safari")
# print(my_car.car_info()) #can access but cannot use self inside staticmethod
# print(Car.car_info())
my_car.model = "nexon"
print(my_car.modelChange()) 
#   File "C:\Users\Nikhil\Python\chapter08(Oop!)\05_solution.py", line 21, in <module>
#     print(my_car.modelChange())
#           ~~~~~~~~~~~~~~~~~~^^
# TypeError: 'str' object is not callable