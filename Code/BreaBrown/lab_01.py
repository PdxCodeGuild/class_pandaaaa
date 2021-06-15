conversions = {
'ft': 0.3048,
'mi': 1609.34,
'm': 1,
'km': 1000,
'yards': 0.9144,
'inches': 0.0254
}


ft_in_m = 0.3048
distance = int(input('What\'s the distance? '))
start_unit = input('Enter the type of unit: ')
end_unit = input('Enter the unit you\'d like to convert to: ')
output = distance * conversions[start_unit]  / conversions[end_unit]
distance = float(distance)
print(f'{distance} {start_unit} in {end_unit} is {output} {end_unit}.')