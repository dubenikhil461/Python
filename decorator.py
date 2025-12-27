from functools import wraps;

def logger(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"calling {func.__name__}")
        result = func(*args,**kwargs)
        print(f"finished {func.__name__}")
        return result
    return wrapper

@logger
def func(type): # func = logger(func)
    print(f"type {type}")

func("hello")   # wrapper("hello")