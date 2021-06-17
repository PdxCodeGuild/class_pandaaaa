def main():
    print(add(1,2,3,4,5))
    exit()

def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

main()