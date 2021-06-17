def func_a():
    print('runs only when funca is called')

def main():
    print("runs only when main is called")

# runs to check if there is a main function:
if __name__ == "__main__":
    main()

print("global scope: runs automatically")

# print("Value in built variable name is:  ",__name__)