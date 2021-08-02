import ashton_lab_1 as lab1
import ashton_lab_2 as lab2
import ashton_lab_3 as lab3
import ashton_lab_4 as lab4
import ashton_lab_5 as lab5
import ashton_lab_6 as lab6
import ashton_lab_7 as lab7
import ashton_lab_8 as lab8
import ashton_lab_9 as lab9
import ashton_lab_10 as lab10
import ashton_lab_11 as lab11
import ashton_lab_12 as lab12
import ashton_lab_24 as lab24
import ashton_lab_55 as lab55

def main():
    option = 0
    while(option != 'x'):
        option = input('\nWhat lab do you want to run? Enter x to exit\noptions: ' +
        '\n1. unit converter'+
        '\n2. list averager'+
        '\n3. number to phrase converter'+
        '\n4. black jack advice'+
        '\n5. pick6' +
        '\n6. credit card number checker' +
        '\n7. ROT+13 converter' +
        '\n8. Peaks and valleys' +
        '\n9. ARI calculator (tkinter window)' +
        '\n10. Contact list' +
        '\n11. Sorting/Searching Algorithms'
        '\n12. ATM lab (tkinter window)'+ 
        '\n24. Rain Data' +
        '\n55. emoticon generator'+
        '\n')
        try:
            if(int(option) in dispatch):
                dispatch[int(option)].main()
        except ValueError:
            pass
        
    exit(0)


#this function prints blank lines
def line_printer():
    for i in range(15):
        print()

dispatch = {
    1:lab1,
    2:lab2,
    3:lab3,
    4:lab4,
    5:lab5,
    6:lab6,
    7:lab7,
    8:lab8,
    9:lab9,
    10:lab10,
    11:lab11,
    12:lab12,
    24:lab24,
    55:lab55,
}

main()