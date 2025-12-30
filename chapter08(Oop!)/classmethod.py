class A:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    
    @classmethod
    def from_dict(cls,detail):
        return cls(
            detail['name'],
            detail['age']
        )   
    
    @classmethod
    def from_list(cls,detail):
        return cls(
           detail[0],
           detail[1]
        )


a = A.from_dict({'name':'nikhil','age':26})
b = A.from_list(['nikhil',26])
print(a.name,a.age)
print(b.name,b.age)