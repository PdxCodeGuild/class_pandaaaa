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
    for i in range(50):
        print(random.choice(emoticon_dictionary['eye']) 
        + random.choice(emoticon_dictionary['nose']) 
        + random.choice(emoticon_dictionary['mouth']))
    return(0)


