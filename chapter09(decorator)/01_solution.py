def fun(func3):
    def fun1():
        print(f"run before {func3.__name__}")
        func3()
        print(f"run after {func3.__name__}")
    return fun1

@fun
def fun3():
    print("i am inside fun3")

fun3()