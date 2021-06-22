convert_dict = { 
  "ft" : 0.3048, 
  "mi": 1609.34, 
  "m": 1, 
  "km": 1000,
  "yd": 0.9144,
  "in": 0.0254
   }

def main():
  # print(str(unit_converter(distance_input())) + "m")
  distance = distance_input()
  unit = unit_input()

  meters = unit_converter(distance, unit)
  print(meters)
  exit(0)

def distance_input():
  distance = input("What is the distance?")
  return float(distance)

def unit_converter(distance_1, unit):
  Answer = distance_1 * convert_dict[unit]
  return Answer

def unit_input():
  valid = 0 
  while not valid:
    unit = input("what are the units? (ft / mi / m / km / yd / in)")
    if not (unit != "ft" and unit != "mi" and unit != "m" and unit != "km" and unit != "yd" and unit != "in"):
      valid = 1 
  return unit


main()


#version three: add support for yards and inches 


