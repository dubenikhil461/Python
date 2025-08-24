# scopes 
name = "nikhil"
def func1():
    name = "nikhil"
    return name

print(func1())
print(name)

#factory function aka closure

def func2():
    num = 0
    def func3():
        nonlocal num
        num += 1
        return num ** 2
    return func3

f = func2()
print(f())
print(f())
print(f())