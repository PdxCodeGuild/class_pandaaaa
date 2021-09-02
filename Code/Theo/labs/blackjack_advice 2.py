import random

def main():
    total = 0
    for i in range(2):
        total = blackjack(total)
    if check_total(total) == False:
        exit()
    while True:
        keep_going = input("Hit or Stay? ")
        if keep_going == 'Stay':
            break
        elif keep_going == 'Hit':
            total = blackjack(total)
            if check_total(total) == False:
                exit()
        else:
            continue
    exit()


def blackjack(total):
    while True:
        card = deal()
        total = add_cards(total,card)
        print(f"You got: {card}")
        break
    return total


def deal():
    cards = [2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']
    return (random.choice(cards))


def add_cards(total,card):
    if card == 'jack' or card == 'queen' or card == 'king':
        total += 10
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


def check_total(total):
    print(f"{total} is total.")
    if total > 21:
        advice(total)
        return False
    if total == 21:
        advice(total)
        return False
    else:
        advice(total)
        return True

main()