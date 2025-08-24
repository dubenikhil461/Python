# reverse a string
word = input("enter the string: ")
reverse_string= ''
# print(string[::-1])
for i in word:
    reverse_string = i + reverse_string
print(reverse_string) 
