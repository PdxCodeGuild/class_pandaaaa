#This file serves as a graveyard for my larger pieces of deleted code

#lab03
#ALTERNATE FUNCTION VERSION
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

#lab3 
#this function was replaced with a function that returns the string instead of printing it inside the function
# #this function converts the argument to a roman numeral
# def roman_converter(num):
#     num2 = str(num) #used to store the number as a string, so it can be indexed
#     length = len(num2)
#     #1 digit 
#     if(length == 1):
#         num2 = int(num2)
#         print(roman_ones_dict[int(num)])
#     #2 digits
#     elif (length == 2):
#         if(num2[1] == '0'):
#             print(roman_tens_dict[int(num2[0])])
#         else:
#             print(roman_tens_dict[int(num2[0])] + roman_ones_dict[int(num2[1])])
#     #3 digits
#     elif (length == 3):
#         if(num2[1] == '0' and num2[2] == '0'):
#             print(roman_hundreds_dict[int(num2[0])])
#         elif(num2[1] == '0'):
#             print(roman_hundreds_dict[int(num2[0])] + roman_ones_dict[int(num2[2])])
#         elif(num2[2] == '0'):
#             print(roman_hundreds_dict[int(num2[0])] + roman_tens_dict[int(num2[1])])
#         else: 
#             print(roman_hundreds_dict[int(num2[0])] + roman_tens_dict[int(num2[1])] + roman_ones_dict[int(num2[2])])

