import sub_mod as mod
from num_dicts import singles_dict, teen_dict, doubles_dict 

error_response = "Only numerical characters, numbers must not start with 0! type 'done' to exit: \n"
error_response_2 = "I can only calculate numbers up to the hundred trillions range (15 digits) \n"

def number_converter():
  num = input("Give me a number and I'll convert it to english: \n")
  num_array = [n for n in num]
  alpha_number = ""
  if num == "0": #check if user entered "0"
    num_array = []
    alpha_number = "zero"
  while len(num_array) > 0:
    if num.isnumeric(): 
      if num[0] == "0": # check if user started number with a 0
        num = input(error_response)
        num_array = [n for n in num]
      elif len(num_array) == 1: 
        number = num_array.pop(0)
        if number != "0" :# check if the last number is not 0 so not to add zero to the end of a number
          alpha_number += singles_dict[number]
      elif len(num_array) == 2:
        number = num_array.pop(0)
        if number == "1": # if the first number of a 2 number is a 1 need to use teen dict for last 2 digits
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2]
        elif number == "0": # if the second number is a 0 remove last digit and evaluate with singles_dict
          number_2 = num_array.pop(0)
          alpha_number += singles_dict[number_2]
        elif number == "0": # if the second number of a 2 digit number is 0 
          alpha_number += doubles_dict[number] + " "
        else: 
          number_2 = num_array.pop(0)
          alpha_number += doubles_dict[number] + " " + singles_dict[number_2]
      elif len(num_array) == 3:
        number = num_array.pop(0)
        if number != "0": 
          alpha_number += singles_dict[number] + " hundred & "
          #Thousands pattern
      elif len(num_array) == 4:
        number = num_array.pop(0)
        if number != "0":
          alpha_number += singles_dict[number] + " thousand, "
      elif len(num_array) == 5:
        number = num_array.pop(0)
        if number == "1":
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2] + " thousand, "
        else:
          #Python version of a ternary opperator to remove a space if number is a 0
          alpha_number += (" " + doubles_dict[number] + " ") if number != "0" else (doubles_dict[number] + " ")
      elif len(num_array) == 6:
        number = num_array.pop(0)
        alpha_number += singles_dict[number] + " hundred &"
        # Millions pattern copy of Thousands but with different words and index checks
      elif len(num_array) == 7:
        number = num_array.pop(0)
        if number != "0": 
          alpha_number += singles_dict[number] + " million, "
      elif len(num_array) == 8:
        number = num_array.pop(0)
        if number == "1":
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2] + " million, "
        else:
          #Python version of a ternary opperator to remove a space if number is a 0
          alpha_number += (" " + doubles_dict[number] + " ") if number != "0" else (doubles_dict[number] + " ")
      elif len(num_array) == 9:
        number = num_array.pop(0)
        alpha_number += singles_dict[number] + " hundred &"
      # Billions pattern  copy of millions 
      elif len(num_array) == 10:
        number = num_array.pop(0)
        if number != "0": 
          alpha_number += singles_dict[number] + " billion, "
      elif len(num_array) == 11:
        number = num_array.pop(0)
        if number == "1":
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2] + " billion, "
        else:
          #Python version of a ternary opperator to remove a space if number is a 0
          alpha_number += (" " + doubles_dict[number] + " ") if number != "0" else (doubles_dict[number] + " ")
      elif len(num_array) == 12:
        number = num_array.pop(0)
        alpha_number += singles_dict[number] + " hundred &"
          # Trillions pattern  copy of Billions 
      elif len(num_array) == 13:
        number = num_array.pop(0)
        if number != "0": 
          alpha_number += singles_dict[number] + " trillion, "
      elif len(num_array) == 14:
        number = num_array.pop(0)
        if number == "1":
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2] + " trillion, "
        else:
          #Python version of a ternary opperator to remove a space if number is a 0
          alpha_number += (" " + doubles_dict[number] + " ") if number != "0" else (doubles_dict[number] + " ")
      elif len(num_array) == 15:
        number = num_array.pop(0)
        alpha_number += singles_dict[number] + " hundred &"
        #We can only calculate numbers up to this high
      elif len(num_array) > 15:
        num = input(error_response_2)
        num_array = [n for n in num]
    elif num == "done":
      num_array = []
    else:
      num = input(error_response)
      num_array = [n for n in num]
  print(alpha_number)
  exit(0)

#--------------------------------------Version2-----------------------------------------------------------------------




#number converter 2  bring in the repeated code as a module and reuse it to get the same answer
  
def n_c_2():
  num = input("Give me a number and I'll convert it to english: \n")
  num_array = [n for n in num]
  alpha_number = ""
  if num == "0": #check if user entered "0"
    num_array = []
    alpha_number = "zero"
  while len(num_array) > 0:
    if num.isnumeric(): 
      if num[0] == "0": # check if user started number with a 0
        num = input(error_response)
        num_array = [n for n in num]
      elif len(num_array) == 1: 
        number = num_array.pop(0)
        if number != "0" :# check if the last number is not 0 so not to add zero to the end of a number
          alpha_number += singles_dict[number]
      elif len(num_array) == 2:
        number = num_array.pop(0)
        if number == "1": # if the first number of a 2 number is a 1 need to use teen dict for last 2 digits
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2]
        elif number == "0": # if the second number is a 0 remove last digit and evaluate with singles_dict
          number_2 = num_array.pop(0)
          alpha_number += singles_dict[number_2]
        elif number == "0": # if the second number of a 2 digit number is 0 
          alpha_number += doubles_dict[number] + " "
        else: 
          number_2 = num_array.pop(0)
          alpha_number += doubles_dict[number] + " " + singles_dict[number_2]
      elif len(num_array) == 3:
        number = num_array.pop(0)
        if number != "0": 
          alpha_number += singles_dict[number] + " hundred & "
      elif len(num_array) > 3 and len(num_array) <= 15:
        #use sub mod function
        digit_location = len(num_array)
        number = num_array.pop(0)
        if len(num_array) in [4,7,10,13] and num_array[0] == "1":
          number_2 = num_array.pop(0)
          alpha_number += mod.p(number, digit_location, number_2)
        else:
          alpha_number += mod.p(number, digit_location)
    elif len(num_array) > 15:
      num = input(error_response_2)
      num_array = [n for n in num]
    elif num == "done":
      num_array = []
    else:
      num = input(error_response)
      num_array = [n for n in num]
  print(alpha_number)
  exit(0)
  


  
#----------------------Run Function------------------------------


number_converter()
# n_c_2()
