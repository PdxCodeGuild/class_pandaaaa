from num_dicts import singles_dict, teen_dict, doubles_dict 

def p(number, digit_location, number_2="none"):
  # ternary opperator with multiple choice options
  num_loc = ("thousand" if digit_location < 6 
    else "million" if digit_location < 9 
    else "billion" if digit_location < 12
    else "trillion")
  
  if digit_location in [4,7,10,13]:
    if number != "0": 
      return F"{singles_dict[number]} {num_loc}, "
  elif digit_location in [5,8,11,14]:
    if number == "1":
      return F"{teen_dict[number_2]} {num_loc}, "
    else:
      #Python version of a ternary opperator to remove a space if number is a 0
      return (" " + doubles_dict[number] + " ") if number != "0" else (doubles_dict[number] + " ")
  elif digit_location in [6,9,12,15]:
    return singles_dict[number] + " hundred &"
