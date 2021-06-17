def count_hand():
    card_value = {'A' : 11,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
    }
    points = 0
    card_1 = input('First card: ')
    card_2 = input('Second card: ')
    card_3 = input('Third card: ')
    card_hand = [card_1, card_2, card_3]
    for card in card_hand:
        points += card_value[card]
        if points >= 10:
            card_value['A'] = 1
    return points
        
            
def give_advice(points):
    if points < 17:
        output = f'Your total points are {points} you should: "Hit"'
    elif points >= 17 and points < 21:
        output = f'Your total points are {points} you should: "Stay"'    
    elif points == 21:
        output = f' You have a "Blackjack!" with {points} points'
    else: 
        output = f'You have {points} points "Bust!"'    
    return output

def run():
    print(give_advice(count_hand()))

run()