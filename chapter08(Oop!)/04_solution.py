class Car:
    def __init__(self,model,brand): #constructor 
        self.model = model #self is context (this is js)
        self.__brand = brand
    
    def get_brand(self):
        return f"{self.__brand}"

    def fullname(self):
        print(f"{self.model} {self.__brand}")
my_car = Car("tata","safari")
# print(my_car.__brand) #AttributeError: 'Car' object has no attribute '__brand'. Did you mean: 'get_brand'?
print(my_car.get_brand())
print(my_car.fullname())