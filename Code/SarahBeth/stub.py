fix = 'hello'
while True:
    if fix != 'name' or fix != 'phone number' or fix != 'email':
            #if fix:
        break
    else: 
        print("Please enter a response from the list of options")
        fix = input("Edit 'name', 'phone number', or 'email'?  ")
        print(fix)

print('name' != 'name')