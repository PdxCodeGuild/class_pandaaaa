import json 

class ContactList: 
    def __init__(self):
        self.contacts = []
    #load
    def load(self):
         # 1) open 'contacts.json' with option 'r' for read
        with open('contacts.json', 'r') as file:
            # 2) get the text from the file
            text = file.read()
        data = json.loads(text)
        # print(data)
        self.contacts = data['contacts']

    def count(self): 
        return len(self.contacts)

    # create
    # def add_contact()
    # update
    # def edit_contact()
    # retrieve
    # def find_contact()
    # delete
    # def delete_contact()


contact_list = ContactList()
contact_list.load()
print(contact_list.count())



    #create(add contact)
    #read 
    #update // edit 
    # delete 