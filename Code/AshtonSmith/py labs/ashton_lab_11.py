# Lab 11: Searching and Sorting
# Big-O Notation is a measure of the complexity of an algorithm, specifically how many steps an algorithm takes depending on the size of the input. For example, performing a linear search on a list of n elements takes, on average, n/2 steps, so we say a linear search is O(n). We throw away multiplicative and additive factors to characterize algorithms independently of the hardware it's running on. Big-O Cheat Sheet



def main():
    option = '1'
    nums = [4, 5, 3, 8, 2, 6, 7, 1]

    print('Before sort: ', end = '')
    print(nums)
    while(option != 'valid'):
        option = input('How would you like to sort your list of numbers?\n1. bubble sort\n2. insertion sort\n3. quick sort\n')
        if(option == '1'):
            buble_sort(nums)
            option = 'valid'
        elif(option == '2'):
            insertion_sort(nums)
            option = 'valid'
        elif(option == '3'):
            quick_sort(nums)
            option = 'valid'
    print('After sort: ', end = '')
    print(nums)
    index = None
    option = ''
    to_find = 0
    while(option != 'valid'):
        option = input('How would you like to search your list of numbers?\n1. linear search\n2. binary search\n')
        if(option == '1'):
            try:
                to_find = int(input('Enter a number to search for'))
            except ValueError:
                pass
            index = linear_search(nums, to_find)
            option = 'valid'
        elif(option == '2'):
            try:
                to_find = int(input('Enter a number to search for'))
            except ValueError:
                pass
            index = binary_search(nums, to_find)
            option = 'valid'
        if index == None:
            print('Number does not exist in the list.')
        else:
            print('Number found at index ' + str(index))



#this function checks the first arg, nums(list) for the arg2, value(int)
#it returns the index or if not found, None
# Implement linear search, which simply loops through the given list 
# and check if each element is equal to the value we're searching for. 
def linear_search(nums, value):
    # index 0  1  2  3  4  5  6  7
    for i in range(len(nums)):
        if i == value:
           return i
    print("number not found") 
    return None



#this function checks the first arg, nums(list) for the arg2, value(int)
#it returns the index or if not found, None
# Implement binary search, 
# which requires that a list is sorted and divides its search range in half each iteration until it finds its target.
def binary_search(nums, value):
    R = len(nums)
    L = 0
    while L <= R :
        m = ((L+R)/2)
        if nums[int(m)] < value:
            L = m + 1
        elif nums[int(m)] > value:
            R = m - 1
        elif nums[int(m)] == value:
            return int(m)
    return None



# This function sorts the arg (nums) with the bubble sort algorithm
# Bubble sort is one of the simplest and least efficient sorting algorithms. We repeatedly loop over the list, 
# comparing each number to the one next to it, and swapping them if needed.
def buble_sort(nums):
    length = len(nums)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, length):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1] 
                nums[i - 1] = nums[i] 
                nums[i] = temp
                sorted = False



# This function sorts the arg(nums) with the insertion sort alogithm
# Implement insertion sort, which like bubble sort is also O(n^2), 
# but is efficient at placing new values into an already-sorted list.
def insertion_sort(nums):
    length = len(nums)
    i = 0
    while i < length:
        j = i 
        while j > 0 and nums[j-1] > nums[j]:     
            temp = nums[j] 
            nums[j] = nums[j-1]
            nums[j-1] = temp
            j -= 1
        i += 1



# Part 5 - Quicksort (optional)
# Quicksort is one of the most efficient sorting algorithms. It works by swapping elements on either side of a pivot value.
#wrapper
def quick_sort(num):
    low = 0
    high = len(num) -1
    quick_sort_recursive(num, low, high)



#recursive function
def quick_sort_recursive(num, low ,high):
    if low < high:
        p = quick_sort_partition(num, low ,high)
        quick_sort_recursive(num, low ,p)
        quick_sort_recursive(num, p+1 ,high)



#partition function(swaps indexes)
def quick_sort_partition(num, low, high):
    pivot = num[int(low + (high - low)/2)]
    i = low - 1
    j = high + 1 
    while(1):
        i+=1
        while num[i] < pivot:
            i+=1
        j-=1
        while num[j] > pivot:
            j-=1
        if i >= j:
            return j
        temp = num[i]
        num[i] = num[j]
        num[j] = temp

