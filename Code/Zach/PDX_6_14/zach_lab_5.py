#Zach Watts
#Lab 5

import random

#Version 1
def main():
    el_accountador()
    exit()

def pick6():
    the_6 = []
    for num in range(6):
        the_6.append(random.choice(range(1,100)))
    return the_6

def num_matches(winning_, ticket_):
    matches = 0
    if winning_[0] == ticket_[0]:
        matches += 1
    elif winning_[1] == ticket_[1]:
        matches += 1
    elif winning_[2] == ticket_[2]:
        matches += 1
    elif winning_[3] == ticket_[3]:
        matches += 1
    elif winning_[4] == ticket_[4]:
        matches += 1
    elif winning_[5] == ticket_[5]:
        matches += 1
    return matches

def winnings(matcheez):
    if matcheez == 0:
        return 0
    elif matcheez == 1:
        return 4
    elif matcheez == 2:
        return 7
    elif matcheez == 3:
        return 100
    elif matcheez == 4:
        return 50000
    elif matcheez == 5:
        return 1000000
    elif matcheez == 6:
        return 25000000


def el_accountador():
    balance = 0
    winner = pick6()
    tix = []
    earnings = 0
    expenses = 0
    for num in range(100000):
        tix.append(pick6())
        balance -= 2
        expenses -= 2
    for ticket in tix:
        balance += winnings(num_matches(winner, ticket))
        earnings += winnings(num_matches(winner, ticket))
    roi = (earnings - expenses)/expenses
    print(balance, roi, earnings, expenses)
    return balance



main()