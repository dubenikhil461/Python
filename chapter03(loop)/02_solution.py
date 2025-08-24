# Movie tickets: $12 for adults (18+), $8 for children; discounts on Wednesday
import sys
age = int(input("Enter your age: "))
day = input("Enter day: ").strip().lower()

if age>=18:
    price = 10 if day=="wednesday" else 12
    print(f'ticket price is {price}')
    sys.exit()
elif age<18:
    price = 6 if day=="wednesday" else 8
    print(f'ticket price is {price}')
    sys.exit()
# exit() is similar, but sys.exit() is preferred in scripts.