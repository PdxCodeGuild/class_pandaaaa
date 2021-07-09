#Lab 5: Random Emoticon Generator

# Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\
#Done:
# Define a list of eyes
# Define a list of noses
# Define a list of mouths
# Randomly pick a set of eyes
# Randomly pick a nose
# Randomly pick a mouth
# Assemble and display the emoticon

import random

emoticon_dictionary = {
    'eye':[':',';','8','x'],
    'mouth':['(',')','D','P','*', 'o', '0', 'c', 'C'],
    'nose':['.','-','@','>']
}



def main():
    again = '1'
    while(again == '1'):
        for i in range(50):
            print(random.choice(emoticon_dictionary['eye']) 
            + random.choice(emoticon_dictionary['nose']) 
            + random.choice(emoticon_dictionary['mouth']))
        again = input('Would you like to generate more? Enter 1 for yes or not 1 for no')
    return(0)


