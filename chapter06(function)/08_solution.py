#named argument 
def argu(name,age):
    print(f"name is {name} \n age is {age}")

argu(age=21,name="nikhil") #named passed argument then position dont matter

def print_kwargs(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")

print_kwargs(name='nikhil',age=23)
print_kwargs(name='nikhil',age=23,weight=100)
