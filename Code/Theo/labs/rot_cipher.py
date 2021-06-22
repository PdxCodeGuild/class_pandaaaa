#Lab 7 - ROT Cipher
#Theo Rowlett

import string

def main():
    output_pos = 0
    cipher_length = 13
    output = ''
    alphabet = string.ascii_lowercase
    alphabet_length = len(alphabet)
    user_input = input("Enter the text to be encoded.").lower()
    print(user_input)
    for char in user_input:
        if char in alphabet:
            output_pos = alphabet.index(char) + cipher_length 
            output_pos %= alphabet_length
            #print(output_pos)
            #print(alphabet[output_pos])
            output += alphabet[output_pos]
        else:
            print("False")
            output += char
    print(output)
    exit()

main()

