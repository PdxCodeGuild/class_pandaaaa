import json
import wikipedia


class GardenBuddy():
    def __init__(self):
        self.plants_dict = []
        self.menu = '''
            Welcome to your Plant Buddy!
            Please choose from the following options: 
                    1. Add a new plant
                    2. Delete a plant 
                    3. Update a plant 
                    4. Search for a plant summary
                    5. Create a "to-do" list
        
                    Enter: '''
            
        self.error = 'Please enter a valid option: '
        # print(self.menu)


    def add_new_plant(self):
        name = input('What\'s the plant\'s name? ').lower()
        last_watered = input('When did you last water your plant? (YYYY/MM/DD HH:mm)').lower()
        plant_dict = {'plant name': name, 'last watered': last_watered}
        self.plants_dict.append(plant_dict)
        # print(last_watered)
        with open("plant_names.json", "a") as f:
            f.write(str(self.plants_dict)) 

x = GardenBuddy()
x.add_new_plant()
x.add_new_plant()
print(x.plants_dict)

#     def delete_plant(self):
#         name = input('Enter the name of the plant you\'d like to delete: ').lower()
#         for i in info:
#             if info == i['info']:
#                 remove.remove(i)
#                 return info
#         with open("plant_names.json", "w") as f:
#             f.write(str(self.plants_dict))


#     def update_plant(self):
#         name = input('Enter the name of the plant you\'d like to update: ')
#         for i :
#             if plant_name == i['plant name']:
#                 info.remove(i)
#                 name = input('Enter plant name update: ')
#                 new_dict = {'name': name, 'last watered': last_watered}
#                 info.append(plants_dict)
#                 return info
#         with open("plant_names.json", "w") as f:
#                 f.write(str(self.plants_dict))


#     def make_to_do_list(self):
#         tasks_lst = []
#         tasks = input('Enter a task to add to do list: ')
#         tasks_lst.append(tasks)
#         print(tasks_lst)
#         with open("plants.json", "w") as f:
#             f.write(str(self.tasks_lst))

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

#     else:
#         print('Please select a valid choice!')
#         return menu


# def search_plant_sum():
#     plant_info = input('Enter a plant you\'d like summarized (Please search by scientific name): ')
#     result = wikipedia.search(plant_info)
#     print(result)
#     for search in result:
#         print(result)
#         if search == plant_info:
#             print(wikipedia.page(search).summary)
#     # print(wikipedia.page(result[0]).summary)
# search_plant_sum()



# active = GardenBuddy()
# active.add_new_plant()
# print(active.plants_dict)