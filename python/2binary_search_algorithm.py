# A binary search function that takes in a list and a target.
# Works by breaking down a list into smaller sets on its midpoints until we find the value that we are looking for
def binary_search(list, target):
    # We need to keep track of the position of the list that we are working with
    
    # Pointing to the first element in the list
    first = 0

    # pointing to the last element of the list
    last=len(list)-1

    # using a while loop to execute until the condition evaluates to false
    # executing the condition while first is less than or equal to last
    # When first = to last, the loop exits because item has not been found
    while first<=last:
        # calculating the midpoint
        # using the floor division(//): rounds to the nearest whole number
        midpoint = (first+last)//2
        # print(first)

        # evaluating whether the value at the midpoint equals the target value
        if list[midpoint]== target:
            return midpoint
        # checking if the value is less than the target to discard the other side of the list
        # midpoint not included because its value does not match the target
        elif list[midpoint] < target:
            first=midpoint+1
        # discarding the other side if value is greater
        
        else:
            last=midpoint-1

    # return none after nothing is found
    return None


# Testing to check whether our algorithm works
def verify(index):
    if index is not None:
        print("Target found at index: ", index)

    else:
        print("Target not found in the list")


# example list
numbers = [1, 2, 3, 5, 7, 8, 9, 10, 23]

# running the binary search and assigning the index to a variable
# result = binary_search(numbers, 7)
# # Verifying whether the value has been found
# verify(result)

result = binary_search(numbers, 1)
# Verifying whether the value has been found
verify(result)