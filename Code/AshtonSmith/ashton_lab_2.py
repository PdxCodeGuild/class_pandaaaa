# Ashton Smith
# Lab 2: Average Numbers
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', 
# then divide that sum by the number of elements in that list. Remember len will give you the length of a list.



#prog main
def main():
    num_list = []
    list_fill_prompt(num_list)
    average = list_averager(num_list)

    print("The average is " + str(average))
    exit(0)



#this function prompts the user to enter numbers and then appends them to the argument. It then returns the modified list
def list_fill_prompt(num_list):
    num = 0
    again = 1 

    while(again):
        try:
            num = input("\nEnter a number or done: ")
            if(num == 'done'):
                again = 0
            else:
                int(num)
        except ValueError:
            print("\nPlease enter a valid number.")
            pass
        if(again):
            num_list.append(int(num))
    return num_list



#this function averages the list (arg1) and returns the average
def list_averager(list_1):
    sum = 0
    for i in list_1:
        sum += i
    return sum / len(list_1)
    

