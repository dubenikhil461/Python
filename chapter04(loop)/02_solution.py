# sum of even number till input

number = int(input("enter the number: "))
even_sum =0
for num in range(number+1):
    if num%2==0: even_sum +=num
print(f"sum of even number till {number} is {even_sum}")