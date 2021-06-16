# Lab 3: Number to Phrase
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.
ones_dict = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
tens_dict = {
    2 : 'twenty',
    3 : 'thirty',
    4 : 'fourty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety',
}
roman_ones_dict = {
    0 : '',
    1 : 'I',
    2 : 'II',
    3 : 'III',
    4 : 'IV',
    5 : 'V',
    6 : 'VI',
    7 : 'VII',
    8 : 'VIII',
    9 : 'IX',
    10: 'X',
}
roman_tens_dict = {
    0 : '',
    1 : 'X',
    2 : 'XX',
    3 : 'XXX',
    4 : 'XL',
    5 : 'L',
    6 : 'LX',
    7 : 'LXX',
    8 : 'LXXX',
    9 : 'XC',
}
roman_hundreds_dict = {
    1 : 'C',
    2 : 'CC',
    3 : 'CCC',
    4 : 'CD',
    5 : 'D',
    6 : 'DC',
    7 : 'DCC',
    8 : 'DCCC',
    9 : 'CM',
}
# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase

#prog main
def main():
    option = 0
    while(option != 4):
        option = int(input("\n1. test time converter\n2. test roman numeral converter\n3. test time converter\n4. exit\n"))
        if(option == 1):
            for i in range(999):
                print(number_converter(i))
        elif(option == 2):
            for i in range(999):
                roman_converter(i)
        elif(option == 3):
            my_time = input("enter a time. format: xx:xx, or x:xx\n")
            time_converter(my_time)
    exit(0)



#this function converts a num XX:XX into english
def time_converter(my_time):
    length = len(my_time)
    hours = ''
    minutes = '' 
    if(length == 5):
        hours = number_converter(int(my_time[0]+my_time[1]))
        minutes = number_converter(int(my_time[3]+my_time[4]))
        #has 4 digits
    elif(length == 4):
        hours = number_converter(int(my_time[0]))
        minutes = number_converter(int(my_time[2]+my_time[3]))
    print(hours + ' hours and ' + minutes + ' minutes.')
        


#this function converts the argument to a roman numberal
def roman_converter(num):
    num2 = str(num) #used to store the number as a string, so it can be indexed
    length = len(num2)
    
    if(length == 1):
        num2 = int(num2)
        print(roman_ones_dict[int(num)])
    elif (length == 2):
        if(num2[1] == '0'):
            print(roman_tens_dict[int(num2[0])])
        else:
            print(roman_tens_dict[int(num2[0])] + roman_ones_dict[int(num2[1])])
    elif (length == 3):
        num3 = num2[1] + num2[2]
        num3 = int(num3)
        #if num3 <= 19:
        #    print(ones_dict[num3])
        if(num2[1] == '0' and num2[2] == '0'):
            print(roman_hundreds_dict[int(num2[0])])
        elif(num2[1] == '0'):
            print(roman_hundreds_dict[int(num2[0])] + roman_ones_dict[int(num2[2])])
        elif(num2[2] == '0'):
            print(roman_hundreds_dict[int(num2[0])] + roman_tens_dict[int(num2[1])])
        else: 
            print(roman_hundreds_dict[int(num2[0])] + roman_tens_dict[int(num2[1])] + ''+ roman_ones_dict[int(num2[2])])





#This function converts an integer from 0-999 to its english representation and then returns it as a string
def number_converter(num):
    num2 = str(num) #used to store the number as a string, so it can be indexed
    length = len(num2)
    to_return = ''   
    if(length == 1):
        num2 = int(num2)
        to_return = (ones_dict[num])
    elif (length == 2):
        if num <= 19:
            to_return = (ones_dict[num])
        else:
            if(num2[1] == '0'):
                to_return = (tens_dict[int(num2[0])])
            else:
                to_return = (tens_dict[int(num2[0])] + ones_dict[int(num2[1])])
    elif (length == 3):
        to_return += (ones_dict[int(num2[0])] + ' hundred ')# end = '')
        num3 = num2[1] + num2[2]
        num3 = int(num3)
        if num3 <= 19:
            to_return += (ones_dict[num3])
        else:
            if(num2[2] == '0'):
                to_return += (tens_dict[int(num2[1])])
            else:
                to_return += (tens_dict[int(num2[1])] + ''+ ones_dict[int(num2[2])])
    return to_return
    #print(num2[0] + num2[1])

# thisversion of the function only prints and does not return the result
# #This function converts an integer from 0-999 to its english representation
# def number_converter(num):
#     num2 = str(num) #used to store the number as a string, so it can be indexed
#     length = len(num2)
    
#     if(length == 1):
#         num2 = int(num2)
#         print(ones_dict[num])
#     elif (length == 2):
#         if num <= 19:
#             print(ones_dict[num])
#         else:
#             if(num2[1] == '0'):
#                 print(tens_dict[int(num2[0])])
#             else:
#                 print(tens_dict[int(num2[0])] + ones_dict[int(num2[1])])
#     elif (length == 3):
#         print(ones_dict[int(num2[0])] + ' hundred ', end = '')
#         num3 = num2[1] + num2[2]
#         num3 = int(num3)
#         if num3 <= 19:
#             print(ones_dict[num3])
#         else:
#             if(num2[2] == '0'):
#                 print(tens_dict[int(num2[1])])
#             else:
#                 print(tens_dict[int(num2[1])] + ''+ ones_dict[int(num2[2])])



main()

