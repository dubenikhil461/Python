# prime number check 

num = int(input("enter the number: "))

if num <=1: 
    print(f"{num} is not prime")
else:
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
             print(f"{num} is not prime number")
             break
    else: 
            print(f"{num} is prime number")
