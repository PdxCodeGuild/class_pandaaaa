#Zach Watts
#Lab 11: Searching and Sorting

def main():
    nums = [1,6, 5, 4,3,2,7,8]
    numbs = [1,2,3,4,5,6,7,8]
    value = 5
    linear_search(nums, value)
    binary_search(numbs, value)
    print(bubble_sort(nums))
    exit

def linear_search(nums_, value_):
    idx_lst = []
    nums_.sort()
    inside = True
    for idx, num in enumerate(nums_):
        if num == value_:
            idx_lst.append(idx)
    if value_ not in nums_:
        inside = False
        return inside
    else: return idx_lst

def binary_search(nums_, value_):
    high = len(nums_) - 1
    low = 0
    while nums_[low] < nums_[high]:
        mid = ((low + high)//2)
        if nums_[mid] < value_:
            low = mid
        elif nums_[mid] > value_:
            high = mid
        else: return nums_[mid]
        print(low, mid, high)
    return "Unsuccessful"

def bubble_sort(nums_):
    n = len(nums_)
    valid = 0
    while not valid:
        swapped = False
        for i in range(1, n-1):
            a = nums_[i - 1] 
            b = nums_[i]
            if a > b:
                nums_[i - 1], nums_[i] = nums_[i], nums_[i - 1]
                #nums_.index(a), nums_.index(b) = nums_.index(b), nums_.index(a)
                swapped = True
            else: 
                continue
        if swapped == False:
            valid = 1
    exit()
                


main()