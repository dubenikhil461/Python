class invalidError(Exception):
    pass

def bill(flavor,cups):
    menu = {"masala":20,"ginger":10}
    try:
        if flavor not in menu:
            raise invalidError("your order is not in the list")
        if not isinstance(cups,int):
            raise TypeError("your order of cups must be an integer")
        total_amount = menu[flavor]* cups 
        print(f"your total amount of cups {cups} is {total_amount}") 
    except Exception as e:
        print("Error ",e)
    finally:
        print("Thank You for visiting")

bill("hello",2)
bill("masala","two")
bill("masala",2)