# version 1
num_list = [5, 0, 8, 3, 4, 1, 6]

def avg_nums(x):
    s = 0
    for i in x:
        s += i
    answer = s / len(x)    
    return answer

# version 2    
def list_population():
    l = []
    while True: 
        ui = input('Enter a number to add to the list or "done" to exit: ')
        if ui == 'done':
            break
        if not ui.isnumeric():
            print('Error, please enter a number!')
            continue
        else: 
            l.append(int(ui))  
    return l

def run():
    l = list_population()
    output = avg_nums(l)
    print(f'The average of the numbers you entered is: {output}')

run()