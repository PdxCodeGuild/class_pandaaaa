#Zach Watts
#Day 2 Lab 1

#Version 1
unit_converter = {
    "feet" : 0.3048
}
feet = input("What is the distance in feet?  ")
feet = int(feet)
print(f'{feet} feet is {round(feet*unit_converter["feet"], 4)} m')

#Version 2
unit_converter_additional = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000
}
distance = int(input("What is the distance?  "))
units = str(input("What are the units?  "))
print(f'{distance} {units} is {round(distance*unit_converter_additional[units],4)} m')

#Version 3
unit_converter_additional = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254

}

distance = int(input("What is the distance?  "))
units = str(input("What are the units?  "))
print(f'{distance} {units} is {round(distance*unit_converter_additional[units],4)} m')

#Version 4
unit_converter_additional = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
}

distance = int(input("What is the distance?  "))
units = str(input("What are the starting units?  "))
new_units = str(input("What are the new units to be?  "))
print(f'{distance} {units} is equal to {round((distance*unit_converter_additional[units])/unit_converter_additional[new_units], 4)} {new_units}!')