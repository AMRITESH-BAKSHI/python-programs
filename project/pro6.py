# type of digit Entered 
user=input("enter the anything")
if user.isalpha():
    print(user," is an","alphabet")
elif user.isnumeric():
    print(user,"is an","number")
elif user.isalnum():
    print(user,"is an","alphanumeric character")
elif user.isspace():
    print("you have entered the space")
else:
    print(user,"it is a special character")
