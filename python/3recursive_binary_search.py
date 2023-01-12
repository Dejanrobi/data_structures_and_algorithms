# RECURSIVE BINARY SEARCH

# returns true if the value exists and false if it doesn't
def recursive_binary_search(list, target):
    # considering if an empty list is passed in
    if len(list) == 0:
        return False
    # Calculating the midpoint
    else:
        midpoint = len(list)//2
        
        # if current value equals the target
        if list[midpoint] == target:
            return True           
        # if current value is less than the target
        elif list[midpoint] < target:
            # discarding the entire lower values by calling the function and passing a list with the other greater values
            # passed list starts at the midpoint+1 index to the end of the last list
            return recursive_binary_search(list[midpoint+1:], target)
        # current value greater than the target
        else:
            return recursive_binary_search(list[:midpoint-1], target)

            
# Verifying if our algorithm works
def verify(result):
    print("Target Found: ", result)
            
# Passing the numbers in the array
numbers = [1, 2, 3, 10, 23, 15, 16, 45, 56, 78]

# result after passing the list and target
result = recursive_binary_search(numbers, 10)
# Verifying the result
verify(result)
    
# result after passing the list and target
result = recursive_binary_search(numbers, 6)
# Verifying the result
verify(result)
    