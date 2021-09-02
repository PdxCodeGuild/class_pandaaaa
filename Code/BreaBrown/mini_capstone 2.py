import csv
import arrow

# with open("plant_water.csv", "r") as file:
#    lines = csv.reader(file)
   

def list_population(parameter):
    watered_list = []  
    for line in parameter:
        info = line.split(",")    
        if len(info) == 2:    
            name = info[0]
            watered = info[1]
        data = {'plant name': name, 'last watered': watered}
        watered_list.append(data)
    return(watered_list)
info = list_population(line)


def add_new_plant():
    global info
    name = input('What\'s the plant\'s name? ').lower()
    watered = input('When did you last water your plant? ').lower()
    plants_dict = {'plant name': name, 'last watered': last_water}
    return watered.append(plants_dict)