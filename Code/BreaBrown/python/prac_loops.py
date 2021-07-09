# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

def main():
    n = 5
    test_double_numbers() 
    test_stars()
    test_extract_less_than_ten()
    exit(0)

def double_numbers(nums):
    nums2 = []
    for i in nums:
        nums2.append(i*2)
        print(nums2)

    return nums2

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n):
    return n*'*'
    


#     x = ''
#     for i in range(n):
#         x += '*'
#         print(x)
#     return x

def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'


# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    other_list = []
    for i in nums:
        if i <10:
            other_list.append(i)
    
    return other_list

def test_extract_less_than_ten():
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]

main()    