# Importing the linked list class that we created earlier
from singly_linked_list import LinkedList;

# # Checking whether it worsk
# l = LinkedList()
# l.add(10)
# print(l)

# Merge sort Algorithm
"""
Sorts a linked List in ascending order
-Recursively divides the linked list into a sublist containing a single node
-Repeatedly merge the sublists to produce sorted sublists until one remains
Returns a sorted linked list
"""
def merge_sort(linked_list):
    # Stopping condition
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Merge  the two top level sublists and return it.
    return merge(left, right)

# Split function
def split(linked_list):
    # Split the unsorted list into sublists
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half

    else:
        # for a linked list, size returns greater than the index
        # i.e a linked list with two nodes: size = 2 (indexes available: 0, 1)
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node

        mid_node.next_node = None

        return left_half, right_half

"""
Merges two linked lists, sorting by data in nodes
Returns a new merged list
"""
def merge(left, right):
    # Create a new linked list that contains nodes from
    # mergin left and right
    merged = LinkedList()

    # add a fake head that is discarded later
    merged.add(0)

    # set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node
    while left_head or right_head:
        #  If the head node of left is None, we are past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node 
            # if the head node of right is None, we are past the tail
            # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to false
            left_head = left_head.next_node

        else:
            # Not at either tail node
            # Obtain node data to perform comparison operation
            left_data = left_head.data
            right_data = right_head.data

            # If data on left is less than right, set current to left node
            if left_data <right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to right node
            else:
                current.next_node = right_head

                # Move right head to next node
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(10)
l.add(2)
l.add(24)
l.add(15)
l.add(30)

print(l)

sorted_linked_list = merge_sort(l)
print(sorted_linked_list)



