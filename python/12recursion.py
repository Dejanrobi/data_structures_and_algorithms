# THE ABILITY OF A FUNCTION TO CALL ITSELF
# SLICE: A way to get a list of values from a list

# def sum(numbers):
#     total = 0
#     for number in numbers:
#         total+=number
#     return total

# print(sum([3, 45, 10, 5, 7, 8]))

# # Slice example
# numslice=[30, 20, 15, 10, 5, 7, 8]

# print(numslice[:3])


#RECURSION
def sum(numbers):
    if not numbers:
        return 0
    # recursion to pass the entire list of numbers except the first one
    print("Calling sum(%s)" % numbers[1:])
    remaining_sum = sum(numbers[1:])
    print("Call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum

print(sum([2, 4, 8, 10, 56, 12]))