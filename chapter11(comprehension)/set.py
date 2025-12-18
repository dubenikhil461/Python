myset = [
    "hello1","hello1","hello2"
]

unique = {unique for unique in myset if len(unique) > 10}
print(unique)