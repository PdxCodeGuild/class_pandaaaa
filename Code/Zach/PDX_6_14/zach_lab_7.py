#Zach Watts
#Lab 7: ROT Cipher

rot_13 = {
    'a' : 'n',
    'b' : 'o',
    'c' : 'p',
    'd' : 'q',
    'e' : 'r',
    'f' : 's',
    'g' : 't',
    'h' : 'u',
    'i' : 'v',
    'j' : 'w',
    'k' : 'x',
    'l' : 'y',
    'm' : 'z',
    'n' : 'a',
    'o' : 'b',
    'p' : 'c',
    'q' : 'd',
    'r' : 'e',
    's' : 'f',
    't' : 'g',
    'u' : 'h',
    'v' : 'i',
    'w' : 'j',
    'x' : 'k',
    'y' : 'l',
    'z' : 'm',
    ' ' : ' '
}

alpha = 'abcdefghijklmnopqrstuvqxyz'

def main():
    rot = rotations()
    msg = message()
    choice = enc_or_dec()
    if choice == 'e':
        encrypt(rot, msg)
    elif choice == 'd':
        decrypt(rot, msg)
    exit()

def rotations():
    valid = 0
    while not valid:
        rot = int(input("Enter the number of rotations:  "))
        try:
            valid = 1
        except:
            ValueError
            print("Input must be a number")
    return rot

def message():
    valid = 0
    while not valid:
    #msg = ""
    #while len(msg) < 1:
        msg = str(input("Enter the message you would like to encrypt\n\
             or decrypt without numbers, special characters or capital letters:  "))
        for char in msg:
            if char not in alpha:
                print("You have entered invalid character(s)")
            else: 
                valid = 1
                break
    return msg

def enc_or_dec():
    valid = 0
    while not valid:
        choice = input("Enter 'e' if you would like to encrypt your\n\
             message or 'd' if you would like to decrypt your message:  ")
        if choice == 'e':
            valid = 1
        elif choice == 'd':
            valid = 1
        else:
            print("That is not a valid choice.")
    return choice

def encrypt(rot_, msg_):
    enc_msg = ""
    for char in msg_:
        for idx, letter in enumerate(alpha):
            if char == letter:
                try: enc_msg += alpha[idx + rot_]
                except:
                    IndexError
                    enc_msg += alpha[idx - 26 + rot_]
        if char == " ":
            enc_msg += " "
    print(enc_msg)
    return enc_msg

def decrypt(rot_, msg_):
    dec_msg = ""
    for char in msg_:
        for idx, letter in enumerate(alpha):
            if char == letter:
                try: dec_msg += alpha[idx - rot_]
                except:
                    IndexError
                    dec_msg += alpha[idx + 26 - rot_]
        if char == " ":
            dec_msg += " "
    print(dec_msg)
    return dec_msg

'''
def decrypt(rot_, msg_):
    dec_msg = ""
    dec_lst = [] 
    for char in msg_:
        dec_lst.append(char)
    for char in dec_lst:

        for idx, letter in enumerate(alpha):
            dec_msg += 
    pass
'''


'''
#----------------------------------------VERSION 1---------------------------------------------#
def encrypt():
    valid = 0
    encrypted = ""
    while not valid:
        user_msg = input("Please input your message in lower case letters:  ")
        try:
            for char in user_msg:
                encrypted += rot_13[char]
            valid = 1
        except:
            KeyError
            print("That value cannot be encrypted!")
    print(encrypted)
    return encrypted
#-----------------------------------------------------------------------------------------------#
'''

main()