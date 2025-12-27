# class Person:
#     def __init__(self , name ,age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"Hello My name is {self.name} and Age {self.age}"

# p = Person("nikhil" , 26)

# print(p.introduce())

# class Animal:
#     def speak(self):
#         return f"Bird is chirping"

# class Dog(Animal):
#     def speak(self):
#         return f"Dog Is Barking"

# d = Dog()
# print(d.speak())


# from typing import override


# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def get_details(self):
#         return f"Employee Name is {self.name} and Salary {self.salary}"
    
# class Manager(Employee):
    
#     def __init__(self,name,salary):
#         super().__init__(name,salary)   
#         self.team_size = 10

#     def get_details(self):
#         return f"team Size is {self.team_size} and {super().get_details()}"



# m = Manager("nikhil",50000)

# print(m.team_size)
# print(m.get_details())






class Engine:
    def start(self):
        print("Engine is started")

class Car:
     basecls = Engine()

     def start(self):
        self.basecls.start()



car = Car()

car.start()
    