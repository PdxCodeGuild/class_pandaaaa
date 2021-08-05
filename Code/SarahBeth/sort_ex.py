import random

# # O(1)
# def random_element(nums):
#     index = random.randint(0, len(nums)-1)
#     return nums[index]
# print(random_element([1, 2, 3, 4])) # 4

# # O(n)
# def calculate_total(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(calculate_total([1, 2, 3, 4])) # 10

# # O(n^2)
# def find_pair(nums, target):
#     output = []
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j and nums[i] + nums[j] == target:
#                 output.append((nums[i], nums[j]))
#     return output

# print(find_pair([5, 6, 2, 3, 4], 7)) # [5, 2]



array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]       

#linear search

def LinearSearch(array, element):
    for i in range (len(array)):
        if array[i] == element:
            return i
    return -1

# Binary search

def binary_search_recursive(array, element, start, end):
    # this situation occurs only when the element doesn't exist in the array
    if start > end:
        return -1
    # check middle element, continue search in the appropriate half of the array
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    # check whether the element is smaller or larger than the middle element
    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

# element = 18
# array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

# print("Searching for {}".format(element))
# print("Index of {}: {}".format(element, binary_search_recursive(array, element, 0, len(array))))


def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step+1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# print("Searching for {} in {}".format(element, array))
# print("Index of {}: {}".format(element, binary_search_iterative(array, element)))


# bubble sort
def bubble_sort(list):
    has_swapped = True
    num_of_iterations = 0
    while(has_swapped):
        has_swapped = False
        #go through the list as many times as there are elements
        for i in range(len(array) - num_of_iterations - 1):
            if array[i] > array[i+1]:
                # Swap
                array[i], array[i+1] = array[i+1], array[i]
                has_swapped = True
        num_of_iterations += 1