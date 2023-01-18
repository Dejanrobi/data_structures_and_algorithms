# This is a linear search Algorithm
# 1. The algorithm start at the start of a list
# 2. Compares the current value with the target value
# 3. If the current value is equal to the target value, the index of the value is returned
# 4. If not, it moves to the next value sequentially and and repeats step 2

def linearSearch(arr, target):
  #     looping through the array
    for i in range(0, len(arr)):
#         checking whether the current value is equal to the target
#         print(arr[i])
        if(arr[i]==target):
#             print(arr[i])
            return i
            break
        
    return None
        
        
arr =[3,4,5,6,8,8,9,10]
# print(linearSearch(arr,6))
result = linearSearch(arr,9)


# A function to verify
def verify(index):
    if(index is not None):
        print("The value was found at index: ", index)       
    else:
        print("The value was not found in the list")
        

verify(result)