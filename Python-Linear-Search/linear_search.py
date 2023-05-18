"""
This program performs a linear search and is part 1 of a lesson in algorithmic thinking.  It
simple iterates through the sorted list, one number at a time until it reaches it target number
or displays a message that no number if found.
"""

def linear_search(list, target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 4)
verify(result)