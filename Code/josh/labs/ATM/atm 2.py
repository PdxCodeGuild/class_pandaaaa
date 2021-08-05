class ATM:
  def __init__(self, balance=0 ):
    self.balance = balance 

  def check_balance(self):
    return self.balance

  def deposit(self, amount):
    self.balance += amount 
    return self.balance
  
  def check_withdrawal(self, amount):
    if self.balance - amount >= 0:
      return True
    else: return False

  def withdraw(self, amount):
    self.balance -= amount
    return self.balance
  
  def calc_intrest(self):
    return self.balance * 0.001
  


