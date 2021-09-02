printstuff()

def printstuff(list):

    print(list)
    return None


class ATM(object):

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

