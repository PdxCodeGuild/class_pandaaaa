import requests
import re
import string


def open_book(book_id): #opens book given an id
    with open(f'{book_id}.txt', encoding='utf-8') as f:
        contents = f.read()
        print(contents)
    return contents

def characters(contents):
    char_count = 0
    for char in contents:
        if char in string.printable:
            char_count += 1
    return char_count

def words(contents):
    word_count = contents.split()
    return len(word_count)

def sentences(contents):
    sentence_count = 0
    for char in contents:
        if char == '.' or char == '?' or char == '!':
            sentence_count += 1
    return sentence_count

def get_ari(contents):
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
    ari = round(4.71 * (characters(contents)/words(contents)) + 0.5 * (words(contents)/sentences(contents)) - 21.43)
    grade = ari_scale[ari]['grade_level']
    age = ari_scale[ari]['ages']
    print(f'The ARI is {ari}\nThis corresponds to a(n) {grade} level of difficulty that is suitable for an average person {age} years old.')
    return ari



def get_books(search):
    print('hey')
    # put the search term into our query string / query parameters
    params = {'query': search}
    # send the request to project gutenberg
    response = requests.get('https://www.gutenberg.org/ebooks/search/', params=params)
    # running regex on the html source code that we get in response
    # to get a list of ids of books that match the search term
    text = response.text
    print(text)
    book_ids = re.findall(r'\/ebooks\/(\d+)', text)
    titles = re.findall(r'<span class="title">(.+)<\/span>', text)
    titles = titles[4:]
    print(book_ids)
    print(len(book_ids))
    print(len(titles))
    output = []
    for i in range(len(book_ids)):
        output.append({'title': titles[i], 'id': book_ids[i]})
    return output
    
def get_book_text(book_id):
    url = f'https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt'
    response = requests.get(url)
    return response.text

def save_book(book_id, text):
    start = text.find('***')
    text = text[start:]
    f = open(f'{book_id}.txt', 'x')
    f.write(text)
    f.close()

def find_new_book():
    search = input('What book would you like to search for? ') # prompt the user for a search term
    books = get_books(search) # list of dictionaries
    # [{'title': 'Pygmalion', 'id': '3825'}, {'title': 'Les Fleurs du Mal. English', 'id': '36098'}
    for i in range(len(books)):
        print(i, books[i]['title'])
    book_id = input('what book would you like to save? enter id: ')
    text = get_book_text(book_id)
    save_book(book_id, text)
    return book_id

def main(): 
    running = True
    while running:
        choice = input("would you like to find & save a new book (f) or get ari for existing book (e)?")
        if choice == 'f':
            find_new_book()
        else: 
            book_id = input ('enter your book id number: ')
            contents = open_book(book_id)
            get_ari(contents)


main()