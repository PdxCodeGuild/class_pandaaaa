# Lab 1: Unit Converter
# This lab will involve writing a program that allows the user to convert a number between units.


conversion_dictionary = {
    #'startingunit_to_endingunit' : conversion factor(float)
    'feet_to_meters' : 0.3048, 
    'miles_to_meters' : 1609.34,
    'kilometers_to_meters': 1000.0, 
    'yards_to_meters': 0.9144,
    'inches_to_meters': 0.0254
}



#program main
def main():
    num = user_prompt_num()
    print('\nEnter the input unit:')
    unit_1 = user_prompt_unit()
    print('\nEnter the output unit:')
    unit_2 = user_prompt_unit()
    
    print("")#padding space
    print(str(num) + " " + str(unit_1) + " = ")
    num = convert_to_meters(num, unit_1)
    print(str(convert_from_meters(num, unit_2)) + " " + str(unit_2))

    exit(0)



#function prompts the user to input a number(distance)- then returns it as a float
def user_prompt_num():
    valid = 0
    while(not valid):
        try:
            feet = float(input("\nWhat is the distance: "))
            valid = 1 
            #float(feet)
        except ValueError:
            print("\nPlease enter a valid number.")
            pass
    return float(feet)



#function prompts the user to input a unit and returns the unit as a string
def user_prompt_unit():
    valid = 0
    while(not valid):
        unit = str(input("What is the unit?(ft/mi/m/km/yd/in): "))
        if (unit != "ft" and unit != 'mi' and unit != 'm' and unit != 'km'and unit != 'yd' and unit != 'in'):
            print("\nPlease enter a valid unit.")
        else:
            valid = 1
    return str(unit)



#this function converts the first argument (already in meters) to the unit specified in the second argument
def convert_from_meters(to_convert, unit_2):
    result = 0
    if(unit_2 == 'm'):
        return to_convert
    elif(unit_2 == 'km'):
        result = to_convert / conversion_dictionary['kilometers_to_meters']
    elif(unit_2 == 'ft'):
        result = to_convert / conversion_dictionary['feet_to_meters']
    elif(unit_2 == 'mi'):
        result = to_convert / conversion_dictionary['miles_to_meters']
    elif(unit_2 == 'yd'):
        result = to_convert / conversion_dictionary['yards_to_meters']
    elif(unit_2 == 'in'):
        result = to_convert / conversion_dictionary['inches_to_meters'] 
    return result 



#this function converts the first argument distance to meters by multiplying by the conversion factor
def convert_to_meters(distance, unit_1):
    result = 0
    if(unit_1 == 'm'):
        result = distance
    elif(unit_1 == 'km'):
        result = distance * conversion_dictionary["kilometers_to_meters"]
    elif(unit_1 == 'ft'):
        result = distance * conversion_dictionary["feet_to_meters"]
    elif(unit_1 == 'mi'):
        result = distance * conversion_dictionary["miles_to_meters"]
    elif(unit_1 == 'yd'):
        result = distance * conversion_dictionary["yards_to_meters"]
    elif(unit_1 == 'in'):
        result = distance * conversion_dictionary["inches_to_meters"]
 
    return result


