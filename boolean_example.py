print( 123 == "123" )

user = input("Enter a string: ")
if len(user) < 5:
    print("Less than 5 chars")
elif len(user) > 5:
    print("Greater than 5 chars")
else: 
    print("5 chars long")
