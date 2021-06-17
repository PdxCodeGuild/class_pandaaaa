import ashton_lab_1 as lab1
import ashton_lab_2 as lab2
import ashton_lab_3 as lab3
import ashton_lab_4 as lab4
import ashton_lab_5 as lab5

def main():
    option = 0
    while(option != 'x'):
        option = input('What lab do you want to run? (1-5) Enter x to exit\n options: ' +
        '\n1. unit converter'+
        '\n2. list averager'+
        '\n3. number to phrase converter'+
        '\n4. black jack advice'+
        '\n5. emoticon generator'+
        '\n')
        try:
            if(int(option) in dispatch):
                dispatch[int(option)].main()
        except ValueError:
            pass
        
    exit(0)

dispatch = {
    1:lab1,
    2:lab2,
    3:lab3,
    4:lab4,
    5:lab5,
}

main()