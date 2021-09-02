import string

def rotn(text, rot_amount):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.whitespace
    output = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            output += char
        else:
            index += rot_amount
            index %= len(alphabet)
            output += alphabet[index]
    return output
        
print(rotn(input("enter a string: "), int(input("enter rotation: "))))





# encrypted_text = 'UryyBh9BEyq.'
# for i in range(26):
#     decrypted_text = rotn(encrypted_text, -i)
#     if 'Hello' in decrypted_text:
#         print('The decrypted text is: ' + decrypted_text)
#         print('The rotation amount was ' + str(i))