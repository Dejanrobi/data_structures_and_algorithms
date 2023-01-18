# SINGLY LINKED LIST

# Creating a class to  represent a node
class Node:
    # An onject for storing a single node for a singly linked list.
    # Initially assigning a none value to the data variable
    # Instant variables: data(holds the data we are storing), next_node(holds the reference to the next node in the list)
    data = None
    next_node = None

    # Adding a constructor
    def __init__(self, data):
        self.data = data

    # String representation of what we want printed to the console
    # %s: substituting something into a string
    # %self.data: we are replacing %s with self.data
    def __repr__(self):
        return "data: %s" %self.data


# Using the Node
# Creating the object of the class since we used the constructor
n1 = Node(10)
n2 = Node(20)
n1.next_node = n2
print(n1)
print(n1.next_node)