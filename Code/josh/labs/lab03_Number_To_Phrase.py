
singles_dict = { 
  "0": "",
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four",
  "5": "five",
  "6": "six",
  "7": "seven",
  "8": "eight",
  "9": "nine",
}

teen_dict ={
  "0": "ten",
  "1": "eleven",
  "2": "twelve",
  "3": "thirteen",
  "4": "fourteen",
  "5": "fifteen",
  "6": "sixteen",
  "7": "seventeen",
  "8": "eighteen",
  "9": "nineteen"
}

doubles_dict ={
  "0": "",
  "2": "twenty",
  "3": "thirty",
  "4": "forty",
  "5": "fifty",
  "6": "sixty",
  "7": "seventy",
  "8": "eighty",
  "9": "ninety"
}

error_response = "Only numerical characters, numbers must not start with 0! type 'done' to exit: \n"
error_response_2 = "Max number length is 9! \n"

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
        if num_array[0] == "1": # if the first number of a 2 number is a 1 need to use teen dict for last 2 digits
          number = num_array.pop(0)
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2]
        elif num_array[0] == "0": # if the second number is a 0 remove last digit and evaluate with singles_dict
          number = num_array.pop(0)
          number_2 = num_array.pop(0)
          alpha_number += singles_dict[number_2]
        elif num_array[1] == "0": # if the second number of a 2 digit number is 0 
          number = num_array.pop(0)
          alpha_number += doubles_dict[number] + " "
        else: 
          number = num_array.pop(0)
          number_2 = num_array.pop(0)
          alpha_number += doubles_dict[number] + " " + singles_dict[number_2]
      elif len(num_array) == 3:
        number = num_array.pop(0)
        if number != "0": 
          alpha_number += singles_dict[number] + " hundred & "
      elif len(num_array) == 4:
        number = num_array.pop(0)
        if number != "0":
          alpha_number += singles_dict[number] + " thousand "
      elif len(num_array) == 5:
        number = num_array.pop(0)
        if number == "1":
          alpha_number += teen_dict[number_2] + " thousand "
        else:
          #Python version of a ternary opperator to remove a space if number is a 0
          alpha_number += (" " + doubles_dict[number] + " ") if number != "0" else (doubles_dict[number] + " ")
      elif len(num_array) == 6:
        number = num_array.pop(0)
        alpha_number += singles_dict[number] + " hundred &"
      elif len(num_array) == 7:
        number = num_array.pop(0)
        if number != "0": 
          alpha_number += singles_dict[number] + " million "
      elif len(num_array) == 8:
        number = num_array.pop(0)
        if number == "1":
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2] + " million "
        else:
          #Python version of a ternary opperator to remove a space if number is a 0
          alpha_number += (" " + doubles_dict[number] + " ") if number != "0" else (doubles_dict[number] + " ")
      elif len(num_array) == 9:
        number = num_array.pop(0)
        alpha_number += singles_dict[number] + " hundred &"
      elif len(num_array) > 9:
        num = input(error_response_2)
        num_array = [n for n in num]
    elif num == "done":
      num_array = []
    else:
      num = input(error_response)
      num_array = [n for n in num]
  print(alpha_number)

number_converter()