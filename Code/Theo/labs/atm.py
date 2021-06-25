import datetime
class ATM:
    def __init__(self,balance=0,interest=0.001,acc_interest = 0,last_transaction='01/01/2001',transactions = {'type':[],'money':[],'time':[]}) -> None:
        self.balance = balance
        self.interest = interest
        self.acc_interest = acc_interest
        self.last_transaction = datetime.datetime.strptime(last_transaction, '%m/%d/%Y')
        self.transactions = transactions

    def __str__(self) -> str:
        return f'Current balance: ${self.balance} at {self.interest}. Account opened on {self.last_transaction}'
    def __repr__(self) -> str:
        return f'ATM({self.balance},{self.interest}'
    def check_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transactions['type'].append('deposit')
            self.transactions['money'].append(amount)
            self.transactions['time'].append(datetime.datetime.today())
            return self.balance
        else:
            return 'error'

    def check_withdrawal(self,amount):
        if self.balance-amount >= 0:
            return True
        return False

    def withdraw(self,amount):
        if amount > 0:
            self.balance -= amount
            self.calc_interest()
            self.transactions['type'].append('withdrawal')
            self.transactions['money'].append(amount)
            self.transactions['time'].append(datetime.datetime.today())
            return amount
        else:
            return 'error'
    
    def calc_interest(self):
        today = datetime.datetime.today()
        for i in range(len(self.transactions['type'])):
            timediff = today - self.transactions['time'][i]
            timediff = float(timediff.years)
            print(timediff)
            # if self.transactions['type'][i] == 'depsosit':
            #     self.acc_interest += self.balance*(1-(self.interest*timediff)) - self.balance
            # elif self.transactions['type'][i] == 'withdrawals':
            #     pass
        return self.acc_interest

    def print_transactions(self):
        for i in range(len(self.transactions['money'])):
            print(f'{self.transactions["type"][i]}: \t ${self.transactions["money"][i]}')

def main():
    client = ATM() # create an instance of our class
    print('Welcome to the ATM')
    while True:
        command = input('Enter a command: ')
        if command == 'balance':
            balance = client.check_balance() # call the check_balance() method
            print(f'Your balance is ${balance}')
        elif command == 'deposit':
            amount = float(input('How much would you like to deposit? '))
            client.deposit(amount) # call the deposit(amount) method
            print(f'Deposited ${amount}')
        elif command == 'withdraw':
            amount = float(input('How much would you like to withdraw? '))
            if client.check_withdrawal(amount): # call the check_withdrawal(amount) method
                client.withdraw(amount) # call the withdraw(amount) method
                print(f'Withdrew ${amount}')
            else:
                print('Insufficient funds')
        elif command == 'interest':
            amount = client.calc_interest() # call the calc_interest() method
            print(amount)

        elif command == 'statement':
            client.print_transactions()

        elif command == 'help':
            print('Available commands:')
            print('balance  - get the current balance')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('statement - see transactions')
            print('exit     - exit the program')
        elif command == 'exit':
            break
        else:
            print('Command not recognized')

main()
