
import string

class Book(object): 
    def __init__(self, file, title):
        self.title = title
        self.file = file
        self.text = ''
        self.chars = 0
        self.words = 0
        self.sentences = 0
        self.ari = 0
    def __str__(self):
        return self.title
    def open_book(self): #opens book given an id
        with open(self.file, encoding='utf-8') as f:
            self.text = f.read()
        return self.text
    def get_characters(self):
        for char in self.text:
            if char in string.printable:
                self.chars += 1
        return self.chars
    def get_words(self):
        self.words = len(self.text.split())
        return self.words
    def get_sentences(self):
        for char in self.text:
            if char == '.' or char == '?' or char == '!':
                self.sentences += 1
        return self.sentences

    def get_ari(self):
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
        self.ari = round(4.71 * (self.chars/self.words) + 0.5 * (self.words/self.sentences) - 21.43)
        grade = ari_scale[self.ari]['grade_level']
        age = ari_scale[self.ari]['ages']
        print(f'The ARI for {self.title} is {self.ari}\nThis corresponds to a(n) {grade} level of difficulty that is suitable for an average person {age} years old.')
        return 

alice = Book('1.txt', 'alice in wonderland')
print(alice.text)
print(alice.get_words())
alice.open_book()
print(alice.get_words())
print(alice.get_characters())
print(alice.get_sentences())
print(alice.ari)
alice.get_ari()
