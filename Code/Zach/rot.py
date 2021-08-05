# alph = 'abcde'
# alph13 = 'nopqr'

def rot13v2(text, num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    translation = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            translation += char
        else:
            print('line 12', index)
            index += num
            index %= len(alphabet)
            print('line 14', index)
            translation += alphabet[index]
    print(translation)

rot13v2('xyz',5)