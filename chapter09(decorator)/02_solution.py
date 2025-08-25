def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling function {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper

@debug
def args():
    print("hello i am item1")

@debug
def kwargs(name,greeting="hello",id=23):
    print(f"{greeting},{name}")

#under the hood
# kwargs = debug(kwargs)

args()
kwargs("nikhil")