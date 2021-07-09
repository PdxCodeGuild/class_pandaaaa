# Lab 6
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
def main():
    again = '1'
    option = '1'
    while(again == '1'):
        card_num_str = ''
        option = input("would you like to use a default card number or enter one? \nEnter a 1 to input a card or the default will be used.")
        if option == '1':
            card_num_str = input('Enter a card number, numbers only')
        else:
            card_num_str = '4556737586899855'
        if(is_valid_card(card_num_str)):
            print('Valid Card')
        else:
            print('Invalid Card')
        again = input("Would you like to test another card? Enter 1 for yes or not 1 for no")
    return 0


#Checks if a card number is valid
def is_valid_card(card_num_str):
    card_num_list = []
    convert_to_list_ints(card_num_str, card_num_list)
    check_digit = slice_last_digit(card_num_list)
    card_num_list = reverse_digits(card_num_list)
    double_every_other_element(card_num_list)
    sub_nine_nums_over_nine(card_num_list)
    sum = sum_all(card_num_list)
    key = second_digit_remover(sum)
    # If key matches the check digit, the whole card number is valid.
    if key == int(check_digit):
        return True
    else: 
        return False
  

# Convert the input string into a list of ints
def convert_to_list_ints(card_num_str, card_num_list):
    length = len(card_num_str)
    for i in range(length):
        card_num_list.append(card_num_str[i])



# Slice off the last digit. That is the check digit.
def slice_last_digit(card_num_list):
    length = len(card_num_list)
    return(card_num_list.pop(length-1))



# Reverse the digits.
def reverse_digits(card_num_list):
    temp_list = []
    i = len(card_num_list)
    while(i > 0):
        temp_list.append(int(card_num_list.pop(i-1)))
        i -= 1
    return temp_list



# Double every other element in the reversed list.
def double_every_other_element(card_num_list):
    j = 0#index tracker
    for i in card_num_list:
        if not(j%2):
            card_num_list[j] *= 2
        j += 1



# Subtract nine from numbers over nine.
def sub_nine_nums_over_nine(card_num_list):
    j = 0#index tracker
    for i in card_num_list:
        if i > 9:
            card_num_list[j] -= 9
        j +=1



# Sum all values.
def sum_all(card_num_list):
    sum = 0
    for i in card_num_list:
        sum += i
    return sum



# Take the second digit of that sum.
def second_digit_remover(num):
    temp = str(num)
    length = len(temp)
    if(length == 2):
        temp = str(temp[1])
    return int(temp)
    

    