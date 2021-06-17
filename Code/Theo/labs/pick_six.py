#Lab 5
import random

winnings = {        #Dollar amounts for num of matches
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000
}

def main():
    pick_six = random_six()
    #print_numbers(*pick_six)
    #user_picks = user_pick()
    user_picks = random_six()
    matches =  compare_nums(user_picks,pick_six)
    #print(matches)
    if matches == 0:
        print("Thanks for playing, better luck next time!")
    else:
        print(f"Congratulations! You had {matches} matches for a total winning of ${winnings[matches]}!")
    return winnings[matches]
    #exit()

def random_six():
    pick_six = []
    for i in range(6):
        pick_six.append(random.randint(1,99))
    return pick_six

def user_pick():
    val = 0
    user_picks = []
    count = 0
    while True:
        if count == 6:
            break
        try:
            val = int(input("Enter a number 1-99: "))
        except(ValueError):
            print("Invalid input.")
            continue
        if val < 1 or val > 99:
            print("Invalid input.")
        else:
            user_picks.append(val)
            count += 1
    return user_picks

def print_numbers(*args):
    for arg in args:
        print(arg)
    return

def compare_nums(user_pick,pick_six):
    count = 0
    for i in range(6):
        if user_pick[i] == pick_six[i]:
            count += 1
    return count
                
def looping():      #This is the test function
    attempts = int(100000)
    expenses = attempts * 2
    winnings = 0
    for i in range(attempts):
        winnings += main()

    print(f"After {attempts:,} attempts with random numbers, the winnings were ${winnings:,}")
    print(f"Your expenses were ${expenses:,}.")
    print(f"Your ROI was {(winnings-expenses)/(expenses)}%")

looping()
#main()