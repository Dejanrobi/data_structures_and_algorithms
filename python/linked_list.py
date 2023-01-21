# CREATING A SINGLY LINKED LIST

# 1. Create the nodes (each node contains two fields: data and the reference to the next node)
class Node:
    # Initializing the data and the reference (class constructor)
    def __init__(self, data):
        self.data = data
        # None because we are creating the nodes, not linking them
        self.ref = None

# 2. Linking the Nodes that we have created
class LinkedList:
    def __init__(self):
        # The linked list will contains:
        # The Head
        # If head is none, then its an empty linked list
        self.head = None
    # Operations performed on a linked list: adding an element, removing and traversal

    # TRAVERSAL OPERATION
    # Start with the head of the linked list
    # Access the data if the head is Not Null else print (Linked List Empty, break)
    # Go to the next node and access the node's data
    # Continue until the last node

    # printing the linked list
    def print__LL(self):
        # checking if head is None
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            n = self.head

            # while there is a reference
            while n is not None:
                # data in current node
                print(n.data)
                # next node (ref in current node)
                n = n.ref




LL1 = LinkedList()
# Empty Linked List
# LL1.print__LL()
LL1.print__LL(2)