class Encryptor:
    def __init__(self):
        self.rot13_dict = { 'a': 'n',
        'b': 'o',
        'c': 'p',
        'd': 'q',
        'e': 'r',
        'f': 's',
        'g': 't',
        'h': 'u',
        'i': 'v',
        'j': 'w',
        'k': 'x',
        'l': 'y',
        'm': 'z',
        'n': 'a',
        'o': 'b',
        'p': 'c',
        'q': 'd',
        'r': 'e',
        's': 'f',
        't': 'g',
        'u': 'h',
        'v': 'i',
        'w': 'j',
        'x': 'k',
        'y': 'l',
        'z': 'm'
        }

def convert(self):
    user_input = list(input('Enter what you want to encrypt here: '))
    output = ''
    for index, value in enumerate(user_input):
        user_input[index] = self.rot13_dict[value]

    for letter in user_input:
        output += letter        

    return output