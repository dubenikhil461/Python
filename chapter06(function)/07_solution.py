def sum_all(*args):
    print(args) # give tuples
    for a in args:
        print(a*2)
    return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7))