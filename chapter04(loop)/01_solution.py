#counting positive numbers

list = [1,2,3,4,-5,6,-7,-1,2]
count = 0
for l in list:
    if l>0: count +=1

print(f'count of positive number is {count}')