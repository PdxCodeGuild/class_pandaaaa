#Zach Watts
#Lab 12: ATM

class ATM:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = 0 # these are member variables
        self.interest_rate = 0.01
        self.transactions = []
    
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        return self.balance + amount

    def check_withdrawal(self, amount):
        if self.balance - amount < 0:
            return False
        else: return True

    def withdraw(self, amount):
        new_amount = 0
        self.balance -= amount
        return amount

    def calc_interest(self):
        self.balance += (self.balance*self.interest_rate)
        return self.balance

    def record_transactions(self, amount):
        self.transactions.append(amount)
        return self.transactions

    def print_transactions(self):
        print(self.transactions)
        exit()

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit?  '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
        atm.record_transactions(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdrawal?  '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
            atm.record_transactions(f'Withdrew ${amount}')
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
atm.print_transactions()
