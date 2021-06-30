#Lab 9
#Theo Rowlett
from io import SEEK_CUR
import string

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def main():
    filename='pg35688.txt'
    ari = ari_calc(filename)
    print(f"The ARI for {filename} is {ari}.")
    print(f"This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty")
    print(f"That is suitable for an average person {ari_scale[ari]['ages']} years old.")
    exit()
    
def ari_calc(filename):
    chars = 0
    words = 0    
    try:
        f = open(filename,'r')
    except(IOError):
        print(f"{filename} not found. Exiting application")
        exit()
    
    contents = f.read()
    f.close()

    words = len(contents.split())
    contents_period = len(contents.split('.'))
    contents_exclamation = len(contents.split('!'))
    contents_question = len(contents.split('?'))
    sentences = contents_period + contents_exclamation + contents_question
    for word in contents:
        for char in word:
            chars += 1
    
    #print (chars)
    #print(words)
    #print(sentences)
    return round(4.71*(chars/words) + 0.5*(words/sentences)-21.43)

main()

