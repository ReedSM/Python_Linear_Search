"""
This program is a simple example of a binary search and is lesson 2 in a study of algorithmic thinking.
This program takes a sorted range, determines the midpoint, ignores the portion below or above the midpoint,
thus creating a new midpoint.  The program continues iterates until it reaches its target or displays a
message that there is no number in the list.
"""

def binary_search(list, target):
  first = 0
  last = len(list)-1

  while first <= last:
    midpoint = (first + last)//2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint -1

  return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index, "\n")
    else:
        print("Target not found in list\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)