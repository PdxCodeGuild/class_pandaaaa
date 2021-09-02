# f = open('phonebook.txt')
# contents = f.read()
# print(contents)

# f.close()

# with open('phonebook.txt', 'r') as phone_book_file:
#     read_line = ''
#     for line in phone_book_file:
#         # print(line)
#         read_line = line
        
#         if read_line == "Tyrone Hopton,00718 04608-5":
#             print('found entry!')
        # print(f'reading time {counter}', line)

with open('phonebook.txt', 'w') as phone_book_file:
    phone_book_file.write('hello world!')

    