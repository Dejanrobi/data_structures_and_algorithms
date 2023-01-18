# Creating a list
new_list = [1, 2, 3, 4]

# Accessing a value from the array
result = new_list[0];

# accessing a value
# In operator calls the contains method defined on the list type which runs the linear search operation.
# For loop can also be used to run through the list manually and find the item
if 1 in new_list:
    print(True)


for n in new_list:
    # print(n)
    if n == 1:
        print(True)
        break


# Inserting an item into the end of a list
numbers=[]
numbers.append(3)
# print(len(numbers))
print(numbers)

# Extend
numbers.extend([4, 5, 6])