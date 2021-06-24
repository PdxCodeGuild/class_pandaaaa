#Ashton Smith
#Lab 9

from tkinter import *
from tkinter import ttk
import string
# Lab 9: Compute Automated Readability Index
# Compute the ARI for a given body of text loaded in from a file. 
# The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. 
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
   
    window = Window()
    window.mainloop()
    return 0



# The score is computed by :
class ari_calculator:
    def __init__(self, my_string):
        super(ari_calculator, self).__init__()
        self.word_count = self.get_words(my_string)
        #print ('Word count: ' + str(self.word_count))
        self.sentence_count = self.sentence_counter(my_string)
        #print('Sentence count: ' + str(self.sentence_count))
        #divide chars/words and mult by 4.71
        num_1 = self.div_char_by_words(my_string, self.word_count) 
        #divide words/sentences and mult by 0.5
        num_2 = self.add_num_words_mult_div(self.sentence_count,self.word_count)
        self.ari = (num_1 + num_2) - 21.43
        self.ari = round(self.ari)  
        #over 14, = 14
        if(self.ari > 14):
            self.ari = 14
        print(ari_scale[self.ari])



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
        for i in my_str:
            # if i == '' :
            #     continue
            # if i[0].isupper() or i[0] == '[':
            #     cap_found = True
            #  if (i[-1] == '.' or i[-1] == '!' or i[-1] == '?' ):
            #     punc_found = True
            # if i[-1] in string.punctuation:

              if (i == '.' or i == '!' or i == '?' ):
                counter += 1
                # punc_found = True
            # if punc_found :
                # counter +=1
                #cap_found = False
                # punc_found = False
        return counter


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("ARI Calculator")
        self.minsize(200,100)
        self.create_combo()

    def open_file(self,selected):
        with open(f'{selected}', encoding='utf-8') as contents:
            f = contents.read()
        contents.close()
        calc = ari_calculator(f)
        print(f)
        return calc
 
    def create_combo(self):
        self.book_id = StringVar()
        self.combobox = ttk.Combobox(self, width = 20, textvariable = self.book_id)
        self.combobox['values'] = ('alice.txt', 'neanderthal_eae.txt','gatsbyCh25.txt')
        
        self.combobox.grid(column = 1, row =  0)

        self.label = ttk.Label(self, text = 'Select the file to calculate')
        self.label.grid(column = 1, row = 2)

        self.label1 = ttk.Label(self, text = 'ARI score: ')
        self.label1.grid(column = 1, row = 14)
        self.label2 = ttk.Label(self, text = 'Words: ' )
        self.label2.grid(column = 1, row = 16)
        self.label3 = ttk.Label(self, text = 'Sentences: ' )
        self.label3.grid(column = 1, row = 18)
        
        self.button = ttk.Button(self, text = 'Calculate ARI', command = self.click_me)
        self.button.grid(column = 2, row =0)
    
    #called when button is clicked
    def click_me(self):
        self.label.configure(text ='selected : ' + self.book_id.get())
        #open file and calculate
        calc = self.open_file(self.book_id.get())
        self.label1.configure(text ='ARI score : ' + str(calc.ari))
        self.label2.configure(text = 'Words: ' + str(calc.word_count))
        self.label3.configure(text = 'Sentences: ' + str(calc.sentence_count))
