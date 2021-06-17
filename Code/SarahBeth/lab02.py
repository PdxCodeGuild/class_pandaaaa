# version 1____
num_list = [5, 0, 8, 3, 4, 1, 6]
sum_ = 0
for num in num_list:
    sum_ += num
# sum_ = sum(num_list) -> using built in function
average = (sum_ / len(num_list))

# version 2______
# nums = []
# again = 1

# while again:
#     try:
#         next_num = input('enter the next number or done:   ')
#         if next_num =='done':
#             again = 0
#         nums.append(int(next_num))
#     except ValueError:
#         print('please enter a valid number')
#         pass
# print(nums)

# print(f'average:{sum(nums)/len(nums)}')

next_num = 1
type = type(next_num)

print(type)

