# REPL:
# Read-Evaluate-Print

# Function anatomy:
# def: the def keyword, telling Python we’re about to start a function definition
# a name for the function
# (: opening parenthesis
# (optional) the names of one or more arguments, separated with ,
# (optional) the names and values of one or more default arguments, separated with (,) 
# ) closing parenthesis
# : a colon

# Function Contents: 
# a new line
# indentation (press tab on your keyboard)
# one or more lines
# (optional) a return statement (with no return, function returns None)


# A Basic Function that accepts no arguments and returns nothing.
def hello_world():
    print("Hello, World!")


# A Function that accepts two arguments, and returns the value of
# those numbers added together.
def add_numbersA(x, y):
    return x - y



# functions can have default values:
def add_numbersB(x, y=6):
    return x + y


#function parameters can have default values that will be used if no value is passed in
def add_numbersC(x, y, operation = "add"):
    if operation =="add":
        return x + y
    elif operation == "sub":
        return x - y

print(add_numbersC(4, 10, 'sub'))
