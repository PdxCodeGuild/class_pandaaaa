#Ashton Smith
#Lab 4 

# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
#  Then, figure out the point value of each card individually. 



cards = {
    'A': 1,
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    '10': 10, 
    'J': 10, 
    'Q': 10, 
    'K': 10
    }



def main():
    user_hand = []
    playing_card_prompt(user_hand)
    advice_giver(display_points(user_hand))
    return(0)



#this function prompts the users to enter three playing cards
#(A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
def playing_card_prompt(user_hand):
    current_card = ''
    for i in range(3):
        valid = 0
        while not(valid):
            current_card = input("\nEnter card number " + str(i+1) + ". \n" + 
            "Options: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K\n")
            if current_card in cards:
                user_hand.append(str(current_card))
                valid = 1
            else:
                print("\nEnter a valid card.\n")
                valid = 0



#This function calculates and then displays and returns the point total
def display_points(user_hand):
    point_total = 0
    for i in user_hand:
        point_total += cards[i]
    
    #check if ace is 1 or 11
    for i in user_hand:
        if(point_total < 21 and i == 'A' and point_total+10 < 22):
            print("Ace counted as 11")
            point_total += 10
    print ("\nTotal Points: " + str(point_total) + '\n')
    return int(point_total)



#this function will give out advice based on points
def advice_giver(points):
    if(points < 17):
        print("Hit")
    elif(points >= 17 and points < 21):
        print("Stay")
    elif(points == 21):
        print("Blackjack!")
    else:
        print("Already Busted")




       