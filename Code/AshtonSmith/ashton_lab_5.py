# Lab 5: Pick6
# Have the computer play pick6 many times and determine net balance.

import random
import time



winnings = {
    0 : 0.00,
    1 : 4.00,
    2 : 7.00,
    3 : 100.00,
    4 : 50000.00,
    5 : 1000000.00,
    6 : 25000000.00
}



class ticket:
    type = 'pick 6'
    price = 2.00 #in usd
    def __init__(self):
        self.nums = []
        for i in  range (6):
            self.nums.append(int((random.randint(1,99) * int(time.time())%99 )))
      

def main():
    print('\n\nPick Six\n')
    valid = 0
    again = '1'
    while again == '1':
        while not valid:
            try:
                play_count = int(input('how many times would you like to play?'))
                valid = 1
            except ValueError:
                pass
        valid = 0
        highest_matches = 0
        match = 0
        earnings = 0.00
        expenses = 0.00
        winning_ticket = ticket()

        for i in range(play_count):
            my_ticket = ticket()
            expenses += my_ticket.price
            match = ticket_checker(my_ticket, winning_ticket)
            if(match > highest_matches):
                highest_matches = match
            earnings += winnings[match]

        balance = earnings - expenses
        print(f'\nEarnings:{earnings}$\nExpenses:{expenses}$\n')
        print(f'Your balance after playing pick six {play_count} times is {balance}$')
        print(f'Highest number of matches: {highest_matches}')
        print( f'{((earnings-expenses)/expenses)*100}% return on investment' )
        again = input('Would you like to play again? Enter 1 for yes or not 1 for no') 
    return 0



#This function compares the numbers in the arguments and returns the number of matches
def ticket_checker(ticket_1, ticket_2):
    match_count = 0
    for i in range(6):
        if ticket_1.nums[i] == ticket_2.nums[i]:
            match_count += 1
    if(match_count == 6):
        print('WIN')
    return match_count


#The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
# and the number of matches between the ticket and the winning numbers determines the payoff.
# Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
# If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
# Calculate your net winnings (the sum of all expenses and earnings).