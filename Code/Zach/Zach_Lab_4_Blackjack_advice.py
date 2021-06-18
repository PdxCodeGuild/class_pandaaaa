#Zach Watts
#Lab 4:  Blackjack Advice

# not currently calling user_feedback

card_dict = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}

def main():
    first_three_Blkjk()
    exit(0)
'''
#Version A; this version cannot catch cards that are not in the choices
#This version is not to be used in conjunction with anything other than the dictionary
#This version also cannot allow the user to enter 'done' to exit
card1 = input("What is your first card?  ")
card2 = input("What is your second card?  ")
card3 = input("What is your third card?  ")
score = card_dict[card1] + card_dict[card2] + card_dict[card3]
if score < 17:
    print(f"{score} Hit!")
elif 17 <= score < 21:
    print(f"{score} Stay")
elif score == 21:
    print(f"{score} Blackjack!")
elif score > 21:
    print(f"{score} Already busted")

'''


#-------------------------------------------------------------------------------------#

'''
#Version 1; this version can be cannot catch "hinging" aces and cannot catch choices not in cards
#this version is to be used with the main function and dictionary

def first_three_Blkjk():
    print("Input your hand or 'done' to exit")
    for i in range(1):
        try:
            card1 = input('What is your first card?  ')
            if card1 == 'done':
                break
            card2 = input('What is your second card?  ')
            if card2 == 'done':
                break
            card3 = input('What is your third card?  ')
            if card3 == 'done':
                break
        except:
            KeyError
            print('That is not a card choice!')
            pass
        three_card_sum = card_dict[card1] + card_dict[card2] + card_dict[card3]
        #if three_card_sum <= 21:
            #card_dict['A'] = 11
        #else: card_dict['A'] = 1
        if three_card_sum < 17:
            print(f'{three_card_sum} Hit!')
        elif 17 <= three_card_sum < 21:
            print(f'{three_card_sum} Stay')
        elif three_card_sum == 21:
            print(f'{three_card_sum} Blackjack!')
        elif three_card_sum >= 21:
            print(f'{three_card_sum} Already busted')
'''

#----------------------------------------------------------------------------------#

#Version 2; this version is to be used with the dictionary, the main function, and the user_feedback function
#this version thus far cannot catch users trying to enter 'done' and exit and results also in asking the user to 
#enter his or her handle three times
def first_three_Blkjk():
    print("Input your hand or 'done' to exit")
    user_hand = []
    user_card = ""
    real_cards = 0
    while real_cards < 3 and user_card != 'done':
        valid = 0
        while not valid:
            user_card = input('Enter your card:  ')
            if user_card == 'done':
                break
            try: 
                current_card = card_dict[user_card]
                user_hand.append(current_card)
                print(user_hand)
                real_cards += 1
                valid = 1
            except: 
                KeyError
                print('Enter a valid card!')
    user_total = sum(user_hand)
    return user_total
    
def user_feedback():
    if first_three_Blkjk() < 17:
        print('Hit!')
    elif 17 <= first_three_Blkjk() < 21:
        print("Stay")
    elif first_three_Blkjk == 21:
        print('Blackjack!')
    elif first_three_Blkjk > 21:
        print("Already busted")



main()