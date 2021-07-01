import json
class ContactList:
    def __init__(self):
        self.contacts = []
    #load
    def load(self):
        #open file with r for read
        with open('contacts.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        print(data)
        self.contacts = data['contacts']
    #this function returns number of contacts
    def count(self):
        return len(self.contacts)
    #this function creates a new contact
    #create(add contact)
conact_list = ContactList()
conact_list.load()
print(conact_list.count())
   


