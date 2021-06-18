#Zach Watts
#Lab 2
#Version 1

nums = [5, 0, 8, 3, 4, 1, 6]
sum_ = 0
for num in nums:
    sum_ += num
average_ = 0
average_ = sum_/len(nums)
print(average_)

#Version 2
numbas = []
next_num = 0
#next_num = int(input("Enter the next number or \'done\' to exit':  "))
while True:
    try:
        next_num = input("Enter the next number or \'done\' to exit':  ")
        if next_num == 'done':
            break
        next_num = int(next_num)
    except: 
        ValueError
        print("You must enter a number or 'done' if finished")
    if isinstance(next_num, str) == True:
        continue
    elif isinstance(next_num, bool) == True:
        continue
    numbas.append(next_num)
    print(numbas)
print(f'average: {sum(numbas)/len(numbas)}')
