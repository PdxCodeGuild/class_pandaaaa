def main():
    # nums = [1, 2, 3, 4, 5, 6, 7, 8]
    unsorted = [6,3,7,2,5]
    # index = linear_search(nums, 3)
    nums = bubble_sort(unsorted)
    for i in range(len(nums)):
        print(nums[i])
    # index = binary_search(nums,3)
    # print(index) # 2

    exit()

def linear_search(nums,value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return -1

def binary_search(nums,value):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (high+low)//2
        # print(f'{nums[low]} L')
        # print(f'{nums[mid]} M')
        # print(f'{nums[high]} H')
        if nums[mid] == value:
            return mid
        elif nums[mid] > value:
            high = mid
            # continue
        else:
            low = mid
            # continue
    return -1

def bubble_sort(to_sort):
    count = 0
    n = len(to_sort)
    # print(n)
    while True:
        swapped = False
        for i in range(1,n):
            if to_sort[i-1] > to_sort[i]:
                temp = to_sort[i]
                to_sort[i] = to_sort[i-1]
                to_sort[i-1] = temp
                swapped = True
                count += 1
                # print(swapped)
        if swapped == False:
            break
    print(f'Swaps: {count}')
    return to_sort

main()