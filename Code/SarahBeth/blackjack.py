card_values = {
    'K': 10,
    'Q': 10,
    'J': 10,
    '9': 9, 
    '8': 8, 
    '7': 7,
    '6': 6,
    '5': 5, 
    '4': 4, 
    '3': 3,
    '2': 2,
    '1': 1
}

def check_aces(cards):
    total = 0
    cards_counter = 0
    if 'A' in cards:
        acesRemoved = [card for card in cards if card != 'A']
        if len(acesRemoved) == 0:
            total += 13
            print('your total is 13: one ace is 11, two aces are 1')
        else: 
            for item in acesRemoved:
                cards_counter += 1
                total += card_values[item]
            if total < 10 and cards_counter == 2:
                print('your ace should be 11')
                total += 11
            elif total < 10 and cards_counter == 1:
                print('one ace is 11, the other is 1')
                total += 12
            elif total == 10 and cards_counter == 1:
                print('your aces should be 1')
                total += 2
            elif total == 10 and cards_counter == 2:
                print('your ace should be 11')
                total += 11
            elif total > 10 and cards_counter == 2:
                print('your ace should be 1')
                total += 1
            elif total > 10 and cards_counter == 1:
                print('both aces are 1')
                total += 2
            else: 
                print('error: somethings missing')
    else: 
        for item in cards:
            total += card_values[item]

    return total

def give_advice(total):
    if total < 17: 
        print('total', total, ':hit!')
    elif total < 21: 
        print('total:', total, ':hit!')
    elif total == 21: 
        print('BLACKJACK')
    else: 
        print('total:', total, 'busted :(')

def main(): 
    cardList = ['A', 'A', 'A']
    total = check_aces(cardList)
    give_advice(total)
main()