import csv
import arrow
import wikipedia


with open("plant_info_lst.csv", "r") as file:
    line = csv.reader(file)

#  with open("")   

# def list_population(parameter):
#     info_list = []  
#     for line in parameter:
#         info = line.split(",")    
#         if len(info) == 2:    
#             name = info[0]
#             watered = info[1]
#         data = {'plant name': name, 'last watered': watered}
#         watered_list.append(data)
#     return(info_list)
# info = list_population(line)


# def add_new_plant():
#     global info
#     name = input('What\'s the plant\'s name? ').lower()
#     watered = input('When did you last water your plant? ').lower()
#     plants_dict = {'plant name': name, 'last watered': last_water
#     return watered.append(plants_dict)
#     add_new_plant()


# def delete_plant():
#     global info
#     name = input('Enter the name of the plant you\'d like to delete: ')
#     for i in info:
#         if info == i['info']:
#             remove.remove(i)
#             return info


# def update_plant():
#     pass


# def search_plant_sum():

#     plant_info = input('Enter a plant you\'d like summarized: ')
#     wikipedia.search(plant_info)
#     print(wikipedia.search(plant_info))
# search_plant_sum()

# def make_personal_notes():
#     pass


# def make_to_do_list():
#     pass


# def nav_menu():
#     print('Welcome to your Plant Buddy!')
#     choice = input('''What would you like to do? 
#                     1. Add a new plant
#                     2. Delete a plant 
#                     3. Update a plant 
#                     4. Search for a plant summary
#                     5. Make a personal note
#                     6. Create a "to-do" list

#                     Enter: ''').lower()
    
#     if choice == '1':
#         add_new_plant()

#     elif choice == '2':
#         delete_plant()

#     elif choice == '3':
#         update_plant()

#     elif choice == '4':
#         search_plant_info()    

#     elif choice == '5':
#         make_personal_notes()

#     elif choice == '6':
#         make_to_do_list()

#     else:
#         print('Please select a valid choice!')
#         return menu()
# nav_menu()        