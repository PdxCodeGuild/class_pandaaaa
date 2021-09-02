Code/SarahBeth/rot13a.py


def rot13v2(text, num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    translation = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            translation += char
        else:
            index += num
            index %= len(alphabet)
            translation += alphabet[index]
    print(translation)

def main():
    text = input('what do you want to translate?')
    rotations = int(input('how many rotations?'))
    # print(rotations)
    rot13v2(text, rotations)

main()