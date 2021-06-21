#Ashton Smith
#Lab 9

from tkinter import *
from tkinter import ttk
# Lab 9: Compute Automated Readability Index
# Compute the ARI for a given body of text loaded in from a file. 
# The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. 
# The general formula to compute the ARI is as follows:

# ARI Formula
def main():
    book_id = 'alice'
   # book_id = 'Code/AshtonSmith/alice'
    contents = ''
    #f = open('Code/AshtonSmith/alice.txt', 'r')
    f = open("alice.txt", "rb")
    
    contents = f.read()
    # with open(f'{book_id}.txt', encoding='utf-8') as contents:
    #     f = contents.read()

    #while not(f.EOFError):
    # my_str += f.read()
    contents.close()
    print(f)
    # print(my_str)
    # my_str = ' Abc def ggg. '
    # calc = ari_calculator(my_str)
    #calc.mainloop()
    return 0
# The score is computed by :
class ari_calculator:
    def __init__(self, my_string):
        super(ari_calculator, self).__init__()
        word_count = self.get_words(my_string)
        sentence_count = self.sentence_counter(my_string)
        #divide chars/words and mult by 4.71
        self.div_char_by_words(my_string, word_count) 
        print(sentence_count)



    #this function returns the number of words in the string
    def get_words(self, my_str):
        return len(my_str.split())



    # this function does the following:  4.71(characters/words)  and returns the result
    def div_char_by_words(self, my_str, word_count):
        count_chars = 0
        for char in my_str:
            if(char != ' '):
                count_chars += 1
        return (word_count/count_chars) * 4.71



    # this function does the following:  0.5(words/sentences)  and returns the result
    def add_num_words_mult_div(self, my_str, word_count):

        return 0



    #this function counts sentences, and then returns the count
    def sentence_counter(self, my_str):
        counter = 0
        my_words = my_str.split(' ')
        cap_found = False
        punc_found = False
        for i in my_words:
            if i == '':
                continue
            if i[0].isupper():
                cap_found = True
            if (i[-1] == '.' or i[-1] == '!' or i[-1] == '?'):
                punc_found = True
            if cap_found and punc_found:
                counter +=1
                cap_found = False
                punc_found = False
        return counter



    # and subtracting 21.43. 
    def sub_21_43(num):
        return float(num) - 21.42



    # If the result is a decimal, always round up. 
    def round_up(num):
        return 0



    # Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
    def greater_than_fourteen():
        return 0



# Scores correspond to the following ages and grad levels:

#     Score  Ages     Grade Level
#      1       5-6    Kindergarten
#      2       6-7    First Grade
#      3       7-8    Second Grade
#      4       8-9    Third Grade
#      5      9-10    Fourth Grade
#      6     10-11    Fifth Grade
#      7     11-12    Sixth Grade
#      8     12-13    Seventh Grade
#      9     13-14    Eighth Grade
#     10     14-15    Ninth Grade
#     11     15-16    Tenth Grade
#     12     16-17    Eleventh grade
#     13     17-18    Twelfth grade
#     14     18-22    College
# Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

# ari_scale = {
#      1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
#      2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
#      3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
#      4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
#      5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
#      6: {'ages': '10-11', 'grade_level':    '5th Grade'},
#      7: {'ages': '11-12', 'grade_level':    '6th Grade'},
#      8: {'ages': '12-13', 'grade_level':    '7th Grade'},
#      9: {'ages': '13-14', 'grade_level':    '8th Grade'},
#     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
#     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
#     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
#     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
#     14: {'ages': '18-22', 'grade_level':      'College'}
# }
# The output should look something like the following:

# --------------------------------------------------------

# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.

# --------------------------------------------------------

main()
