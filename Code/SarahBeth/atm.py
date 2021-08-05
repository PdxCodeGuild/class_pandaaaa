class ATM():
    def __init__(self):
        self.balance = 0
        self.interest = 0.001
        self.transactions = []

    def calc_interest(self):
        """ Returns the amount of interest calculated on the account
        """
        ret = round(self.balance + self.balance * self.interest, 2)
        self.transactions.append(f'User calculated interest: ${ret}')
        return ret

    def check_balance(self):
        """ Returns the account balance
        """
        self.transactions.append(f'User checked balance: ${self.balance}')
        return self.balance


    def deposit(self, amount):
        """ Deposits the given amount in the account
        """
        self.transactions.append(f'User deposited ${amount}')
        self.balance += amount

    def print_transactions(self):
        """ Print list of user transactions
        """
        for line in self.transactions:
            print(line)
        
    def check_withdrawal(self, amount):
        """ Returns true if the withdrawn amount won't put the account in the negative
        """
        return self.balance > amount

    def withdraw(self, amount):
        """ Withdraws the amount from the acount and returns it
        """
        if self.check_withdrawal(amount):
            self.transactions.append(f'User withdrew ${amount}')
            self.balance -= amount
            return amount
        else:
            self.transactions.append(f'User unsuccessfully tried to withdraw ${amount}')            
            return 'Insufficient funds.'

class Piggybank(ATM):
    def __init__(self):
        super().__init__()
        self.smashed = False
    
    def smash_bank(self):
        self.balance = 0
        self.smashed = True

piggybank = Piggybank()

piggybank.deposit(10)
print(piggybank.balance)
print(piggybank.smashed)
piggybank.smash_bank()
print(piggybank.balance)
print(piggybank.smashed)
# print(piggybank.smashed)


# atm = ATM() # create an instance of our class
# print('Welcome to the ATM')
# while True:
#     command = input('Enter a command: ')
#     if command == 'balance':
#         balance = atm.check_balance() # call the check_balance() method
#         print(f'Your balance is ${balance}')
#     elif command == 'deposit':
#         amount = float(input('How much would you like to deposit? '))
#         atm.deposit(amount) # call the deposit(amount) method
#         print(f'Deposited ${amount}')
#     elif command == 'withdraw':
#         amount = float(input('How much would you like '))
#         if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
#             atm.withdraw(amount) # call the withdraw(amount) method
#             print(f'Withdrew ${amount}')
#         else:
#             print('Insufficient funds')
#     elif command == 'interest':
#         amount = atm.calc_interest() # call the calc_interest() method
#         atm.deposit(amount)
#         print(f'Accumulated ${amount} in interest')
#     elif command == 'help':
#         print('Available commands:')
#         print('balance  - get the current balance')
#         print('deposit  - deposit money')
#         print('withdraw - withdraw money')
#         print('interest - accumulate interest')
#         print('exit     - exit the program')
#     elif command == 'exit':
#         break
#     else:
#         print('Command not recognized')
