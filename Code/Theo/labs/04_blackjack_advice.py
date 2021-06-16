import random

def main():
    total = 0
    cards = [2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']
    for i in range(2):
        total = blackjack(cards,total)
    print(f"{total} is total.")
    if total > 21:
        advice(total)
        exit()
    else:
         advice(total)
    
    while True:
        keep_going = input("Hit or Stay? ")
        if keep_going == 'Stay':
            break
        elif keep_going == 'Hit':
            total = blackjack(cards,total)
            print(f"{total} is total.")
            if total > 21:
                advice(total)
                exit()
            else:
                advice(total)
        else:
            continue
    #test_aces()
    exit()
    
def blackjack(cards,total):
    while True:
        card = deal(cards)
        total = add_cards(total,card)
        print(f"You got: {card}")
        break
    return total


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
        print("Recommend Hit!")
    elif total < 21:
        print("Recommend Stay!")
    elif total == 21:
        print("Blackjack!")
    else:
        print("Busted!")

def test_aces():
    assert add_cards(0,'ace') == 11
    assert add_cards(11,'ace') == 12
    assert add_cards(12,'ace') == 13
main()