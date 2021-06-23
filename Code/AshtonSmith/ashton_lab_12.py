# Let's represent an ATM with a class containing two attributes: 
#   a balance and an interest rate. 
#      A newly created account will default to a balance of 0 
# and an interest rate of 0.1%. 
# Implement the initializer, as well as the following functions:
from tkinter import *
import tkinter as tk
from tkinter import messagebox


#################################################################
#Window class
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.atm = ATM()
        self.title("ATM")
        self.minsize(500,500)
        self.create_radio()
        self.create_text_box()

   
   
    def create_text_box(self):
        self.box = tk.Entry().grid(row = 10 , column = 10)
        
        self.textbutton = tk.Button(text='OK', command= self.text_event).grid(row=10, column=12, sticky=tk.W, pady=4)
        
    def text_event(self):
        
        name = StringVar(self, value='not available')
        name = Entry(self, textvariable=name)
        self.name_Tf = self.box
        name = self.name_Tf.get()
        return messagebox.showinfo('message',f'Hi! {name}, Welcome to python guides.')
# ws = Tk()
# ws.title('get text demo')
# ws.geometry('200x200')

# def welcomeMessage():
#     name = name_Tf.get()
#     return messagebox.showinfo('message',f'Hi! {name}, Welcome to python guides.')
    

# Label(ws, text="Enter Name").pack()
# name_Tf.pack()

# Button(ws, text="Click Here", command=welcomeMessage).pack()

        self.label4.configure(text = name)
        #my_str = self.box

    def create_radio(self):
        self.radValues = IntVar()
        self.rad1 = tk.Radiobutton(self, value = 1, variable = self.radValues , command = self.rad_event)
        self.rad1.grid(column = 6, row = 5, sticky = W, columnspan = 3)
        self.label = tk.Label(self, text = 'Balance')
        self.label.grid(column = 5, row = 5)

        self.rad2 = tk.Radiobutton(self, value = 2, variable = self.radValues , command = self.rad_event)
        self.rad2.grid(column = 6, row = 6, sticky = W, columnspan = 3)
        self.label = tk.Label(self, text = 'Withdraw')
        self.label.grid(column = 5, row = 6)
       
        self.rad3 = tk.Radiobutton(self, value = 3, variable = self.radValues , command = self.rad_event)
        self.rad3.grid(column = 6, row = 7, sticky = W, columnspan = 3)
        self.label = tk.Label(self, text = 'Deposit')
        self.label.grid(column = 5, row = 7)

        self.rad3 = tk.Radiobutton(self, value = 4, variable = self.radValues , command = self.rad_event)
        self.rad3.grid(column = 6, row = 8, sticky = W, columnspan = 3)
        self.label = tk.Label(self, text = 'Interest')
        self.label.grid(column = 5, row = 8)

        self.label4 = tk.Label(self, text = 'here')
        self.label4.grid(column = 50, row = 20)

    def rad_event(self):
        temp = ''
        radSelected = self.radValues.get()
        if radSelected == 1:
            temp = str(self.atm.check_balance())
            self.label4.configure(text = 'Current blance = ' + temp)
        elif radSelected == 2:
            #temp = str(self.atm.withdraw())
            self.label4.configure(text = temp + '$ withdrawn')
        elif radSelected == 3:
            #self.atm.deposit()
            self.label4.configure(text = temp + '$ withdrawn')
        elif radSelected == 4:
            #temp = self.atm.calc_interest()
            #self.atm.deposit(temp)
            temp = str(temp)
            self.label4.configure(text = temp + '$ intrest earned')

        #self.label.grid(column = 50, row = 20)



    def take_input():
        return 0
         #= inputtxt.get("1.0", "end-1c")



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
# window = Window()
# window.mainloop()
use_atm()