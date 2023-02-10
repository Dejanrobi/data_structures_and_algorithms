# BOGO SORT (Worst algorithm)
# Randomises the order of the list repeatedly until it is sorted
# Takes the name of the file, loads it and returns a sorted array

import random
import sys   
# A function to check whether the list is sorted
def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True

# A function to sort the list
def bogo_sort(values):
    # Tracking the number of attempts made to sort the list
    attempts = 0
    # looping through the list while its not sorted
    while not is_sorted(values):
        print(attempts)
        # shuffling the order of items in the list
        random.shuffle(values)

        attempts += 1
    # when the list is sorted after randomizing, we return True
    return values


#Values
numbers = [3, 5, 20, 6,17, 7, 24, 10]
print(bogo_sort(numbers))
