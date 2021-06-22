#Zach Watts
#Lab 3

# ones digits returns a whole list

word_dict = {
    0 : ["zero"],
    1 : ["one", "", "one-hundred"],
    2 : ["two", "twenty", "two-hundred"],
    3 : ["three", "thirty", "three-hundred"],
    4 : ["four", "fourty", "four-hundred"],
    5 : ["five", "fifty", "five-hundred"],
    6 : ["six", "sixty", "six-hundred"],
    7 : ["seven", "seventy", "seven-hundred"],
    8 : ["eight", "eighty", "eight-hundred"],
    9 : ["nine", "ninety", "nine-hundred"],
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen"
}

def main():
    num = number()
    #zero_to_99(num)
    print(one_hundred_to_999(num))
    exit()

def number():
    valid = 0
    while not valid:
        try:
            num = int(input("Enter an integer between 0 and 999:  "))
            #if num < 0 or num > 99:
                #print('Integer must be between 0 and 99!')
                #continue
            valid = 1
        except(ValueError):
            print("Input must be an integer")
            break
    return num

def zero_to_99(num):
    tens_dig = num//10
    ones_dig = num % 10
    if tens_dig == 0 and ones_dig == 0:
        return ""
    elif num < 20:
        return word_dict[num]
    elif num >= 20:
        #print(tens_dig)
        if ones_dig == 0:
            return word_dict[tens_dig][1]
        elif tens_dig == 0:
            return f'{0}{word_dict[ones_dig][0]}'
        elif ones_dig > 0:
            return f'{word_dict[tens_dig][1]}-{word_dict[ones_dig][0]}'

def one_hundred_to_999(num):
    if num < 100:
        return zero_to_99(num)
    elif num >= 100:
        hundred = num//100
        ten_and_ones = num%100
        return f'{word_dict[hundred][2]} {zero_to_99(ten_and_ones)}'



main()