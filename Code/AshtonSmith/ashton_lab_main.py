import ashton_lab_1 as lab1
import ashton_lab_2 as lab2
import ashton_lab_3 as lab3
import ashton_lab_4 as lab4
import ashton_lab_5 as lab5
import ashton_lab_6 as lab6
import ashton_lab_55 as lab55

def main():
    option = 0
    while(option != 'x'):
        line_printer()
        option = input('\nWhat lab do you want to run? Enter x to exit\noptions: ' +
        '\n1. unit converter'+
        '\n2. list averager'+
        '\n3. number to phrase converter'+
        '\n4. black jack advice'+
        '\n5. pick6' +
        '\n6. credit card number checker'
        '\n55. emoticon generator'+
        '\n')
        try:
            if(int(option) in dispatch):
                line_printer()
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
    55:lab55,
}

main()