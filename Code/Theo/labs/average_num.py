#Theo Rowlett
#Lab 2
import math

def main():
    nums = []
    sum = 0
    while True:
        return_val = add_num()
        if return_val == 'done':
            break
        else:
            try:
                nums.append(int(return_val))
            except:
                print("That's not a number, try again")

    # loop over the elements
    for num in nums:
        print(num)
        sum += num

    average = sum / len(nums)
    print(f"The average whole number is {int(average)}.")

    exit()

def add_num():
    return input("Enter a number, or 'done': ")

main()