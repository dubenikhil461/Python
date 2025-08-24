# list uniqueness checker

from enum import unique


list = [1,2,3,4,5,2,6]
for i in list:
    if list.count(i)>1:
        print(f"given list is not unique as {i} repeat more than 1")
        break
else: print("list is unique")

#method 2
unique_item = set()
for item in list:
    if item in unique_item:
        print(f"list is not unique")
        break
    else: unique_item.add(item)