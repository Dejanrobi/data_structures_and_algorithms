# LINKED LIST IMPLEMENTATION

# Creating a node
class Node:
    def __init__(self, item):
        self.item = item
        # first setting the address of next node to None
        self.next = None

class LinkedList:
    def __init__(self):
        # first setting the head of the Linked List to None
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connecting the nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item

    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
