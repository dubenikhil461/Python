#1 age group calculation
userinput = input("Enter the Age: ")
userinput_int = int(userinput)
if userinput_int < 13:
    print("child")
elif 13 <= userinput_int <= 19:
    print("teenager")
elif 20 <= userinput_int <= 59:
    print("adult")
else:
    print("senior")
