import random

emoji_dict = {
    'eye':[':',';'],
    'mouth':['(',')','D','P'],
    'nose':['.','-']
}

def main():
    for i in range(5):
        print(random.choice(emoji_dict['eye']) 
        + random.choice(emoji_dict['nose'])
        + random.choice(emoji_dict['mouth']))
    exit()

main()