#Ashton Smith
#Lab 9

from tkinter import *
from tkinter import ttk
# Lab 9: Compute Automated Readability Index
# Compute the ARI for a given body of text loaded in from a file. 
# The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. 
# The general formula to compute the ARI is as follows:
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
# ARI Formula
def main():
    book_id = 'alice'
    with open(f'{book_id}.txt', encoding='utf-8') as contents:
        f = contents.read()
    contents.close()
    print(f)
    calc = ari_calculator(f)
    return 0



# The score is computed by :
class ari_calculator:
    def __init__(self, my_string):
        super(ari_calculator, self).__init__()
        word_count = self.get_words(my_string)
        print ('Word count: ' + str(word_count))
        sentence_count = self.sentence_counter(my_string)
        print('Sentence count: ' + str(sentence_count))
        #divide chars/words and mult by 4.71
        num_1 = self.div_char_by_words(my_string, word_count) 
        #divide words/sentences and mult by 0.5
        num_2 = self.add_num_words_mult_div(sentence_count,word_count)
        roi = (num_1 + num_2) - 21.43
        roi = round(roi)  
        #over 14, = 14
        if(roi > 14):
            roi = 14
        print(ari_scale[roi])



    #this function returns the number of words in the string
    def get_words(self, my_str):
        return len(my_str.split())



    # this function does the following:  4.71(characters/words)  and returns the result
    def div_char_by_words(self, my_str, word_count):
        count_chars = 0
        for char in my_str:
            if(char != ' '):
                count_chars += 1
        print('Character count: ' + str(count_chars))
        return (count_chars/word_count) * 4.71



    # this function does the following:  0.5(words/sentences)  and returns the result
    def add_num_words_mult_div(self, sentence_count, word_count):
        return 0.5 * (word_count/sentence_count)



    #this function counts sentences, and then returns the count
    def sentence_counter(self, my_str):
        counter = 0
        my_words = my_str.split(' ')
        cap_found = False
        punc_found = False
        for i in my_words:
            if i == '' :
                continue
            if i[0].isupper() or i[0] == '[':
                cap_found = True
            if (i[-1] == '.' or i[-1] == '!' or i[-1] == '?' ):
                punc_found = True
            if cap_found and punc_found:
                counter +=1
                cap_found = False
                punc_found = False
        return counter


