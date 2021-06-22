#Zach Watts
#Lab 6:  Credit Card Validation

def main():
    crd_nums = convert_2_lst()
    valid = check(crd_nums)
    display(valid)
    exit()

def convert_2_lst():
    valid = 0
    crd_nums = []

    while not valid:    
        crd = input("Please enter your credit card number with no spaces:  ")
        try:
            num_crd = int(crd)
            for char in crd:
                crd_nums.append(char)
            valid = 1
        except:
            ValueError
            print("You have entered a character that is not a number. \n\
            please re-enter your crdit card number")
    crd_ints = []
    for char in crd_nums:
        crd_ints.append(int(char))
    if len(crd_ints) != 16:
        return ("You have not entered a valid number.")
    return crd_ints
   
def check(crd_nums_):
    last_dig = crd_nums_[-1]
    print(last_dig)
    valid = 0
    crd_nums_.pop()
    print(crd_nums_)
    crd_nums_.reverse()
    print(crd_nums_)
    cred_nums_dubs = []
    for idx, num in enumerate(crd_nums_):
        if idx % 2 == 0:
            num *= 2
        cred_nums_dubs.append(num)
    print(cred_nums_dubs)
    sum_ = 0
    cred_nums_subs = []
    for num in cred_nums_dubs:
        if num > 9:
            num -= 9
        cred_nums_subs.append(num)
    print(cred_nums_subs)
    sum_ = sum(cred_nums_subs)
    print(sum_)
    sum_ %= 10
    print(sum_)
    if sum_ == last_dig:
        valid = 1
    else: valid = 0
    return valid

def display(valid_):
    if not valid_:
        print("Your card number is invalid!")
    else: print("Your card number is valid!")
    exit()

main()