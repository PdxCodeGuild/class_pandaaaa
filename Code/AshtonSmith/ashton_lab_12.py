#Ashton Smith
#Lab12
#ATM lab
from tkinter import *
import tkinter as tk



def main():
    window = Window()
    window.mainloop()

#################################################################
#Window class
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.atm = ATM()
        self.title("ATM")
        self.minsize(250,150)
        self.create_radio()
        self.text_box_exists = False
       

   
    #this function is used to create a text box and button if the button is clicked it calls button clicked
    def create_text_box(self):
        self.box = Text(width= 5, height= 1)
        self.text_box_exists = True
        radSelected = self.radValues.get()
        if(radSelected == 2):#withdraw
            self.box.grid(row = 6 , column = 14)
            self.textbutton = tk.Button(text='OK', command= self.button_clicked)
            self.textbutton.grid(row=6, column=19, sticky=tk.W, pady=4)
        if(radSelected == 3):
            self.box.grid(row = 7 , column = 14)
            self.textbutton = tk.Button(text='OK', command= self.button_clicked)
            self.textbutton.grid(row=7, column=19, sticky=tk.W, pady=4)
            
    
    
    
    #this function is calls the atm methods. when a rad box is selected: 
    #       withdraw/deposit: it then creates a text box with a button. 
    # The button takes the input as a string and then deletes the text box. (and uncheck the rad)
    def button_clicked(self):
        name = StringVar(self)
        name = self.box.get('1.0', 'end-1c')
        radSelected = self.radValues.get()
        if(radSelected == 2):#withdraw
            if self.atm.check_withdrawal(float(name)):
                self.atm.withdraw(float(name))
                self.label4.configure(text = str(name) + '$ withdrawn.')
            else:
                self.label4.configure(text = 'Insufficient Funds')
            self.box.destroy()
            self.textbutton.destroy()
            self.text_box_exists = False
        elif(radSelected == 3):#deposit
            self.atm.deposit(float(name))
            self.label4.configure(text = 'Deposited:' + str(name) + '$.')
            self.box.destroy()
            self.textbutton.destroy()
            self.text_box_exists = False


    #This function creates radio buttons with the labels: Balance, Withdraw, Deposit, and Interest
    def create_radio(self):
        self.radValues = IntVar()
        #button
        self.bal_rad = tk.Radiobutton(self, value = 1, variable = self.radValues , command = self.rad_bal_int)
        self.bal_rad.grid(column = 6, row = 5, sticky = W, columnspan = 3)
        #text
        self.label = tk.Label(self, text = 'Balance')
        self.label.grid(column = 5, row = 5)
        #button
        self.rad2 = tk.Radiobutton(self, value = 2, variable = self.radValues , command = self.rad_dep_with)
        self.rad2.grid(column = 6, row = 6, sticky = W, columnspan = 3)
        #text
        self.label = tk.Label(self, text = 'Withdraw')
        self.label.grid(column = 5, row = 6)
        #button
        self.rad3 = tk.Radiobutton(self, value = 3, variable = self.radValues , command = self.rad_dep_with)
        self.rad3.grid(column = 6, row = 7, sticky = W, columnspan = 3)
        #text
        self.label = tk.Label(self, text = 'Deposit')
        self.label.grid(column = 5, row = 7)
        #button 
        self.rad3 = tk.Radiobutton(self, value = 4, variable = self.radValues , command = self.rad_bal_int)
        self.rad3.grid(column = 6, row = 8, sticky = W, columnspan = 3)
        #text
        self.label = tk.Label(self, text = 'Interest')
        self.label.grid(column = 5, row = 8)
        #label used for displaying data from button events(atm functions)
        self.label4 = tk.Label(self, text = '')
        self.label4.grid(column = 50, row = 20)
    
    

    #radio event for balance and interest 
    def rad_bal_int(self):
        radSelected = self.radValues.get()
        if(radSelected == 1):
            temp = self.atm.check_balance()
            self.label4.configure(text = 'Balance :' + str(temp) + '$.')
        elif(radSelected == 4):
            self.atm.balance = self.atm.balance + self.atm.calc_interest()
            self.label4.configure(text = 'Interest Added')
        
        #self.text_box_exists = True
        if(self.text_box_exists == True):
            self.text_box_exists = False
            self.box.destroy()
            self.textbutton.destroy()



    #radio event for deposit and withdraw
    def rad_dep_with(self):
        temp = ''
        self.radSelected = self.radValues.get()
        if(self.text_box_exists == True):
            self.text_box_exists = False
            self.box.destroy()
            self.textbutton.destroy()
        self.my_text_box = self.create_text_box()



#################################################################
#ATM class
class ATM():
    def __init__(self):
        super(ATM, self).__init__()
        self.balance = 0.0
        self.interest_rate = 0.1
    
    
    
    # check_balance() returns the account balance
    def check_balance(self):
        return self.balance 
   
   
   
    # deposit(amount) deposits the given amount in the account
    def deposit(self, amount):
        self.balance = self.balance + amount 
  
  
  
    # check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self,amount):
        return (self.balance - amount) >= 0.0
 
 
 
    # withdraw(amount) withdraws the amount from the account and returns it
    def withdraw(self, amount):
        self.balance = self.balance - amount



    # calc_interest() returns the amount of interest calculated on the account
    def calc_interest(self):
        return self.balance * (self.interest_rate)



#################################################################
#This function is used to display a repl for the atm functions
def use_atm():
    atm = ATM() # create an instance of our class
    print('Welcome to the ATM')
    while True:
        command = input('Enter a command: ')
        if command == 'balance':
            balance = atm.check_balance() # call the check_balance() method
            print(f'Your balance is ${balance}')
        elif command == 'deposit':
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount) # call the deposit(amount) method
            print(f'Deposited ${amount}')
        elif command == 'withdraw':
            amount = float(input('How much would you like '))
            if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
                atm.withdraw(amount) # call the withdraw(amount) method
                print(f'Withdrew ${amount}')
            else:
                print('Insufficient funds')
        elif command == 'interest':
            amount = atm.calc_interest() # call the calc_interest() method
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest')
        elif command == 'help':
            print('Available commands:')
            print('balance  - get the current balance')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('exit     - exit the program')
        elif command == 'exit':
            break
        else:
            print('Command not recognized')
