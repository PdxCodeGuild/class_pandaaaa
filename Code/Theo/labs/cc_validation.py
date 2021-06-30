#Lab 6
#Theo Rowlett

def validate(cc_num):
    cc_int = []
    length = len(cc_num)
    sum = 0
    #Step 2 - Slice off the check digit
    check_digit = int(cc_num[len(cc_num)-1])
    cc_num = cc_num[0:len(cc_num)-1]
    length -= 1
    print(cc_num)
    #Step 3 - Reverse the digits
    cc_num = cc_num[::-1]
    print(cc_num)
    #Step 1 - Convert to int
    try:
        for i in range(len(cc_num)):
            cc_int.append(int(cc_num[i]))
        print(cc_int)
    except(ValueError):
        print(f"{cc_num} is not a valid credit card number")
        return 0

    #Step 4 - Double every other element
    for i in range(0,length,2):
        cc_int[i] = cc_int[i]*2
    print(cc_int)
    #Step 5 - Subtract 9 for every number over 9
    for i in range(length):
        if cc_int[i] > 9:
            cc_int[i] -= 9
    print(cc_int)
    #Step 6 - Sum all values
    for i in range(length):
        sum += cc_int[i]
    print(sum)
    #Step 7 - Take the second digit of that sum
    compare_dig = sum % 10
    if compare_dig == check_digit:
        return 'Valid'
    return 'Invalid'

def test():
    cc_num = '1234567890'
    print(validate(cc_num))

test()
