# SELECTION SORT
# Start with the sorted and the unsorted array
# Loop through the unsorted array
# Move the minimum value to the end of the sorted array
# Repeat the process again

def selection_sort(values):
    sorted_list = []
    # printing before the loop executes
    # print("%-25s %-25s" % (values, sorted_list))
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        # adding the value to the end of a sorted list
        sorted_list.append(values.pop(index_to_move))
        # print("%-25s %-25s" % (values, sorted_list))
    return sorted_list

def index_of_min(values):
    # start by setting the first value as minimum
    min_index = 0
    # looping through the remaining values
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index



# Numbers
numbers=[3, 45, 10, 34, 15, 5, 23, 9, 10]

print(selection_sort(numbers))