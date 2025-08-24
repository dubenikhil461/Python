# list uniqueness checker

list = [1,2,3,4,5,2,6]
for i in list:
    if list.count(i)>1:
        print(f"given list is not unique as {i} repeat more than 1")
        break
else: print("list is unique")