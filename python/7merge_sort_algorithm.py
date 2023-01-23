# THE MERGE SORT ALGORITHM

# Takes in a list
"""
    Sorts the list in ascending order
    Returns a new sorted list

    Has three main steps
    Divide: finds the midpoint of the list and divides into sublist
    Conquer: recursively sorts the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step
    
    A recursive function has a basic pattern
    1. We start with a base case that includes a stopping condition.
    2. We then have some logic that breaks down the problem and recursively calls itself
    3. Our stopping condition is our end goal of a sorted array
"""
def merge_sort(list):
    # stopping condition
    if len(list) <= 1:
        return list

    # Dividing the list by splitting in the midpoint
    left_half, right_half = split(list)

    # Conquer step (sort each sublist and return a new sorted sublist)
    # this is called again and again until we have a single list
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    # Merging the sorted sublists
    return merge(left, right)

"""
Divide the unsorted list at midpoint into sublists
Returns two sublists  - left and right
Steps:
1. Determing the midpoint of the array
"""

def split(list):

    mid = len(list)//2

    # left list: (slices the list without including the midpoint of the list)
    left = list[:mid]
    # right: starts at the midpoint going to the end of the list
    right = list[mid:]

    # Returning the sublists
    return left, right


#MERGE FUNCTION
# Takes the items in the splitted list, sorts and merges them recussively
"""
Merges two lists(arrays), sorting them in the process
Returns a new merged list
"""
def merge(left, right):
    # our function will return a new list
    l = []
    # In the process of merging, we need to sort the values in both lists
    # to sort, we compare each value from each list

    # index variables to keep track of each values we are using in each lists
    i = 0
    j = 0
    
    # Keep executing the loop until false
    # 1st Loop: accounts only 
    while i < len(left) and j < len(right):
        # comparing the first value in both lists
        if left[i] < right[j]:
            l.append(left[i])
            i+=1

        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l



def verify_sorted(list):
    n = len(list)

    if n==0 or n==1:
        return True

    return list[0] < list[1] and verify_sorted (list[1:]) 

first_list = [23, 12, 35, 10, 8, 21, 45, 16]
final_list = merge_sort(first_list)
print(verify_sorted(first_list))
print(verify_sorted(final_list))