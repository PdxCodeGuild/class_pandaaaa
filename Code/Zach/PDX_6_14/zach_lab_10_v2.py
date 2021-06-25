#Zach Watts
#Lab 10: Contact List

import json

class ContactList():
    def __init__(self, file):
        self.contacts = []
        self.file = file
    
    def load(self):
        with open(self.file, 'r') as file:
            text = file.read()
        data = json.loads(text)
        self.contacts = data['contacts']

    def count(self):
        return len(self.contacts)

    def delete_contact(self):
        name = input('Please type in the name of the contact to be deleted:  ')
        for item in self.contacts:
            if name == item["name"]:
                self.contacts.remove(item)
                return f'{name} has been deleted!'
            else: return f'{name} is not in this list!'

    def edit_contact(self):
        valid_ = 0
        while not valid_:
            contact = input("Which contact would you like to edit?  ")
            for dict in self.contacts:
                if contact == dict["name"]:
                    fix = input("Edit 'name', 'phone number', or 'email'?  ")
                    valid_ = 1
        valid = 0
        while not valid:
            if fix == 'name' or fix == 'phone number' or fix == 'email':
                break
            else: 
                print("Please enter a response from the list of options")
                fix = input("Edit 'name', 'phone number', or 'email'?  ")
                print(fix)
        edit = input(f"What is {fix} to be changed to?  ")
        if fix == 'name':
            dict[fix] = edit
        elif fix == 'phone number':
            dict[fix] = edit
        elif fix == 'email':
            dict[fix] = edit
        print(f"{contact}'s {fix} has been changed to {edit}")
        exit()

    def add_contact(self):
        name = input('Please type in the name of the contact to be added:  ')
        new_contact = {}
        for dict in self.contacts:
            if name == dict["name"]:
                return f'{name} already exists!'
            else: 
                break
        number = input(f"Enter {name}'s phone number:  ")
        email = input(f"Enter {name}'s email:  ")
        new_contact["name"] = name
        new_contact["phone_number"] = number
        new_contact["email"] = email
        self.contacts.append(new_contact)
        print(f"{name} has been added to the contact list!")
        exit()

    def retrieve_contact(self):
        valid = 0
        while not valid:
            contact = input("Enter the contact you'd like to access:  ")
            for dict in self.contacts:
                if contact == dict["name"]:
                    print(dict)
                    valid = 1
            if valid == 0:
                print(f"{contact} does not exist in this contact list!")
        return None

    def write(self, contacts, file):
        for item in self.contacts:
            self.file.write(item)
        self.file.close()
        print("Your changes have been saved!")
        exit()


contacts = ContactList('contacts.json')
contacts.load()
print(contacts.count())
#old_contacts = ContactList('contacts2.json')
#old_contacts.load()
#print(old_contacts.count())

while True:
    selection = input("Please select and option from the following menu:  \n\
        'Access Contact'\n\
        'Edit Contact'\n\
        'Delete Contact'\n\
        'Create Contact'\n\
        'Exit' \n\
        Selection:  ")
    if selection == 'Access Contact':
        contacts.retrieve_contact()
        break
    elif selection == 'Edit Contact':
        contacts.edit_contact()
        break
    elif selection == 'Delete Contact':
        contacts.delete_contact()
        break
    elif selection == 'Create Contact':
        contacts.add_contact()
        break
    elif selection == 'Exit':
        contacts.write()
        break
    else: print("Invalid Selection")




