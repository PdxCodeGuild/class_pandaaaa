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
    user_hand = first_three_Blkjk()
    score_ = scoring(user_hand)
    user_feedback(score_)
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

#Version 2; this version is to be used with the dictionary, the main function, the scoring function and the user_feedback function

def first_three_Blkjk():
    print("Input your hand or 'done' to exit")
    user_hand = []
    user_card = ""
    for i in range(3):
        print(f'for loop {i}')
        if user_card == 'done':
            break
        valid = 0
        while not valid:
            user_card = input('Enter your card. Choices are: 2,3,4,5,6,7,8,9,10,J,Q,K,A.  ')
            if user_card == 'done':
                break
            try: 
                current_card = user_card
                user_hand.append(current_card)
                valid = 1
            except: 
                KeyError
                print('Enter a valid card!')
    return user_hand

def scoring(user_hand):
    aces_removed = []
    ace_count = 0
    score = 0
    for card in user_hand:
        if card == 'A':
            user_hand.remove(card)
            ace_count += 1
        aces_removed = user_hand
    for card in aces_removed:
        score += card_dict[card]
    if ace_count == 3:
        score = 13
    elif ace_count == 2 and score == 10:
        score = 12
    elif ace_count == 2 and score < 9:
        score += 12
    if ace_count == 1 and score >= 11:
        score += 1
    if ace_count == 1 and score <= 10:
        score += 11
    return score
    

def user_feedback(tot):
    if  tot < 17:
        print(f'{tot} Hit!')
    elif 17 <= tot < 21:
        print(f'{tot} Stay')
    elif tot == 21:
        print(f'{tot} Blackjack!')
    elif tot > 21:
        print(f'{tot} Already busted')



main()