# Quick sort algorithm
# To implement it, we write a recursive function
# HOW QUICK SORT WORKS
"""
We take the first element in the list and make it a pivot
Divide the list into a sublist
First list segment contain all elements lesser than the pivot
Second segment contains all elements greater than the pivot
We call the quick sort on the list 
"""


import sys
# from load import load_numbers

# numbers = load_numbers(sys.argv[1])

def quicksort(values):
    # list without or with one element do not need to be sorted
    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]


    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quicksort(less_than_pivot)+[pivot] + quicksort(greater_than_pivot)


# numbers=[3, 45, 10, 34, 15, 5, 23, 9, 10]

numbers =[10, 12, 4, 6, 2, 6, 8, 10, 11, 9]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
