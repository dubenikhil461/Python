# multiplication table
input_num = int(input("enter the number for table: "))

for l in range(1,11):
    if l==5: continue
    print(f"{input_num}*{l}={input_num*l}")
