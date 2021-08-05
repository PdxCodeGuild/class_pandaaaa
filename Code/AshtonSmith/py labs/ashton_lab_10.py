# Lab 10: Contact List

def main():
    my_list = contact_list('contacts.csv')
    my_list.crud_repl()
    my_list.save('contacts.csv')
    return 0

#Contact class
class contact_list:
    def __init__(self, csv=None):
        """
        :csv: str filepath of csv to load contacts from
        """
        self.contacts = []
        self.header = ['name', 'phone', 'email']
        if csv:
            self.load(csv)
      
    
    
    #this function loads data from a .csv file 
    def load(self, path):
        if path.endswith('.csv'):
            with open(path) as f:
                lines = f.read().split('\n')
            contacts = []
            #print(lines)
            header = lines[0].split(',')
            if header != self.header:
                if len(self.contacts) > 0:
                    return 'CSV not compatible'
            for i in range(1, len(lines)):
                row = lines[i].split(',')
                contact = dict(zip(header, row))
                contacts.append(contact)
            self.contacts += contacts
            self.header = header


    #update an existing contact
    def update(self, name):
        found = False
        temp = ''
        for i in self.contacts:
            if i['name'] == name:
                found = True
                print(i)
                temp = input('What would you like to update?')
                if temp in i:
                    i[temp] = input(f'Enter the updated {temp}: ')
                else:
                    print('invalid entry')
        if not found: print('The name entered was not found')
   
   
   
    #remove a contact
    def remove(self, name):
        temp = ''
        x = 0
        for i in self.contacts:
            if i['name'] == name:
                found = True
                print(i)
                while temp != 'y' and temp != 'n':
                    temp = input('Contact found, are you sure you want to delete it? y/n')
                if(temp == 'y'):
                    self.contacts.pop(x)
                break
            x += 1



    #create new person
    def create(self):
        temp = ''
        contact = dict()
        for i in self.header:
            temp = input(f'Enter the {i}: ')
            contact[i] = temp
        self.contacts.append(contact)



    #save - overwrite entire file
    def save(self, path):
        print(self.header)
        if path.endswith('.csv'):
            with open(path, 'w') as f:
                # print (f)
                row = ','.join(self.header)
                f.write(row)
                f.write('\n')
                x = 0
                length = len(self.contacts)
                for j in self.contacts:
                    row = []
                    for i in range(len(j)):
                        row.append(j[self.header[i]])
                    row = ','.join(row)
                    print(row)
                    f.write(row)
                    #only write new line if not last contact
                    if x+1 < length: 
                        f.write('\n')
                    x+=1



    #this repl allows the user to use the member functions    
    def crud_repl(self):
        option = 'y' 
        while(option != 'x'):
            print('1. Create a record')
            print('2. Find a user')
            print('3. Update a record')
            print('4. Delete a record')
            option = input('Enter x to exit')
            if(option != 'x'):
                if option == '1':
                    self.create()
                elif option == '2':
                    self.find_user()
                elif option == '3':
                    self.update(input('Enter the name you want to update'))
                elif option == '4':
                    self.remove()
        return 0



    #this function searches for a user by name
    def find_user(self):
        to_find = input("Enter the name that you want to find: ")
        found = False
        for i in self.contacts:
            if i['name'] == to_find:
                print(i)
                found = True
                break
        if not found:
            print('User doesnt exist')
        