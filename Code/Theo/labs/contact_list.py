import json

class ContactList():
    def __init__(self,filename='contacts.json'):
        self.contacts = []
        self.filename = filename
    def __str__(self) -> str:
        return str(self.contacts)
    def __repr__(self) -> str:
        return f'ContactList({self},{self.filename})'
    
    def file_io(self):
        with open (self.filename) as f:
            text = f.read()
        data =  json.loads(text)
        self.contacts = data['contacts']
        
    def count(self):
        return len(self.contacts)
        
    def create(self):
        this_name = input('Enter a name: ')
        this_phone_number = input('Enter a phone number: ')
        this_email = input('Enter an email: ')
        contact = {
            'name' : this_name,
            'phone_number' : this_phone_number,
            'email' : this_email
        }
        self.add_contact(contact)
        
    def add_contact(self,contact):
        self.contacts.append(contact)
    
    def retrieve(self):
        find_name = input("Enter the name to search for: ")
        for i in range(self.count()):
            if find_name.find(self.contacts[i]['name']) != -1:
                print(self.contacts[i])
                return i
        print('name not found')
        return -1
        
    def update(self):
        i = self.retrieve()
        if i  == -1:
            self.create()
        else:
            if input('Do you want to update the name (y/n)?') == 'y':
                self.contacts[i]['name'] = input('Enter the new name: ')
            if input('Do you want to update the phone number (y/n)?') == 'y':
                self.contacts[i]['phone_number'] = input('Enter the new phone number: ')
            if input('Do you want to update the email address (y/n)?') == 'y':
                self.contacts[i]['email'] = input('Enter the new email: ')
                
    def delete(self):
        i = self.retrieve()
        if i == -1:
            return 'no entries removed'
        else:
            self.contacts.pop(i)
            return 'contact removed successdully'
            
def main():
    list = ContactList()
    list.file_io()
    while True:
        command = input("Enter a command: ")
        if command == 'print':
            for i in range(list.count()):
                print(str(list.contacts[i]))
        if command == 'add':
            list.create()
        elif command == 'search':
            list.retrieve()
        elif command == 'update':
            list.update()
        elif command == 'remove':
            print(list.delete())
        elif command == 'help':
            print('Available commands:')
            print('print - display contact list')
            print('add - add a new contact')
            print('search - find a contact by name')
            print('update - update a contact')
            print('remove - remove a contact by name')
            print('exit - End program')
        elif command == 'exit':
            break
        else:
            pass
        
    exit()
    
main()