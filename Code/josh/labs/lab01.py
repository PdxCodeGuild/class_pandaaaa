def unit_converter():
  unit = input("Meter Converter V1 give me a number in feet and I'll convert it to meters, What's your number in feet?")
  meters = float(unit) * 3.6576
  print(F'{unit} feet equals {meters} meters')


def unit_converterV2():
  unit =input("Meter Converter V2 what is your number to convert?")
  conversion = input(F'OK what is {unit} in? "ft", "mi", "m" or "km"')
  correct_conversion = False
  while  not correct_conversion:
    if conversion == "ft" or conversion == "mi" or conversion == "m" or conversion == "km":
      correct_conversion = True
    else:
      conversion = input('That is not an accepted conversion please enter "ft", "mi", "m" or "km"')
  convert_dict ={"ft" : 0.3048,
  "mi": 1609.34, "m": 1.0, "km": 1000.0}
  converted_num = float(unit) * convert_dict.get(conversion)
  print(f'{unit} in {conversion} equals {converted_num} in meters')


unit_converterV2()