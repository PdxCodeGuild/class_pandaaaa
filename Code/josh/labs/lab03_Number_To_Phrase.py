
singles_dict = { 
  "0": "zero",
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
  "2": "twenty",
  "3": "thirty",
  "4": "forty",
  "5": "fifty",
  "6": "sixty",
  "7": "seventy",
  "8": "eighty",
  "9": "ninety"
}

def number_converter():
  num = input("Give me a numerical number and I'll convert it to english \n")
  num_array = [n for n in num]
  alpha_number = ""
  if num == "0": #check if user entered "0"
    num_array = []
    alpha_number = singles_dict["0"]
  while len(num_array) > 0:
    if num.isnumeric(): 
      if num[0] == "0":
        num = input("Only numerical characters, numbers must not start with 0! or type 'done' to exit \n")
        num_array = [n for n in num]
      elif len(num_array) == 1:
        number = num_array.pop(0)
        if number != "0" :#check if the last number is not 0 
          alpha_number += singles_dict[number]
      elif len(num_array) == 2:
        if num_array[0] == "1": # if the first number of a 2 digit number is a 1
          number = num_array.pop(0)
          alpha_number += teen_dict[number]
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
          alpha_number += singles_dict[number] + " " + "hundred "
      elif len(num_array) == 4:
        number = num_array.pop(0)
        if number != "0":
          alpha_number += singles_dict[number] + " thousand "
      elif len(num_array) == 5:
        number = num_array.pop(0)
        if number == "1":
          number_2 = num_array.pop(0)
          alpha_number += teen_dict[number_2] + " thousand "
        else:
          alpha_number += " " + doubles_dict[number] + " " 
      elif len(num_array) == 6:
        number = num_array.pop(0)
        alpha_number += singles_dict[number] + " hundred"
    elif num == "done":
      num_array = []
    else:
      num = input("Only numerical characters, numbers must not start with 0! or type 'done' to exit \n")
      num_array = [n for n in num]
  print(alpha_number)

number_converter()