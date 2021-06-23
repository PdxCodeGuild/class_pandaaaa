import json

class ContactList():
    def __init__(self,input_file='contacts.json',output_file='contacts.json'):
        self.contacts = []
        self.input_file = input_file
        self.output_file = output_file
    def __str__(self) -> str:
        return str(self.contacts)
    def __repr__(self) -> str:
        return f'ContactList({self},{self.input_file},{self.output_file})'
    
    def read_file(self):
        with open (self.input_file) as f:
            text = f.read()
        data =  json.loads(text)
        self.contacts = data['contacts']
        
    def write_file(self):
        with open(self.output_file, "w") as f:
            new_data = {'contacts':[]}
            new_data['contacts'] = self.contacts
            json.dump(new_data, f, indent=4)
    
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
    list.read_file()
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
    list.write_file()   
    exit()
    
main()