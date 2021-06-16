import random

def main():
    card = 0
    total = 0
    cards = [2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']
    card = deal(cards)
    total = add_cards(total,card)
    print(f"What's your first card? {card}")
    card = deal(cards)
    total = add_cards(total,card)
    print(f"What's your second card? {card}")
    card = deal(cards)
    total = add_cards(total,card)
    print(f"What's your third card? {card}")
    print(f"{total} {advice(total)}")
    exit()
    
def deal(cards):
    return (random.choice(cards))

def add_cards(total,card):
    if card == 'jack':
        total += 11
    elif card == 'queen':
        total += 12
    elif card == 'king':
        total += 13
    elif card == 'ace':
        if total <= 10:
            total += 11
        else:
            total += 1
    else:
        total += card
    return total

def advice(total):
    if total < 17:
        return "Hit!"
    elif total < 21:
        return "Stay!"
    elif total == 21:
        return "Blackjack!"
    else:
        return "Busted!"
main()