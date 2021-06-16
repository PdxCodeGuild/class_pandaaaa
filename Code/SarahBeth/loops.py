#x = 0
#while True:
   # x+=1
    #print(x)
    #ctrlz-> breaks out of loop 
convert_dict = { 
  "ft" : 0.3048, 
  "mi": 1609.34, 
  "m": 1, 
  "km": 1000,
  "yd": 0.9144,
  "in": 0.0254
   }


# for num in range(10):
    # print(num)

string = 'zach'
# for char in string:
    # print(char)

list_items = [99, 98, 25, 23, 40]
doubled_list = []
for element in list_items:
    doubled_list.append(element * 2)
# print(doubled_list)
list_list = [['brea', 'red', 'tacos'], ['Ashton', 'blue', 'wraps'], ['Zach', 'teal', 'cheesecake']]

# for list in list_list:
#     for item in list:
#         if item == 'red':
#             print(item)
#         else: 
#             print('lesser color')

# for unit in convert_dict: 
#     print(unit)
# x = 4
# y = 6
# z = 7
# for i in range(x, y, z):
#     print('hello')
fruit =  input('what fruit do you want?')
fruits = ['apples', 'bananas', 'pears', 'dragon fruit', 'kiwi']

for i in range(len(fruits)):
    print(i)

counter = 0
# for item in fruits:
#     counter += 1
#     if item == fruit: 
#         print('we have that fruit')
#         break 
# print(counter)

for item in fruits: 
    if item == 'pear':
        fruits.remove(item)

nums = [1, 2, 3, 4, 33, 32, 6, 90]
nums.pop(1)
print(nums)