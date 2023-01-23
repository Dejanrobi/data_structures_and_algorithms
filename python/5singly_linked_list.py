# SINGLY LINKED LIST
# Creates a Node
# Links the nodes
# Checks whether a list is empty
# Checks the size of the list

# Creating a Nodes for a linked list(contains the data and the ref to the next Node)
class Node:
    data = None
    next_node = None

    # Initializing the data
    def __init__(self, data):
        self.data = data

    # Representing the return data
    def __repr__(self):
        return "data: %s" % self.data


# Linked List class(used to join the nodes together)
class LinkedList:
    # Initializing the head of the list
    def __init__(self):
        self.head = None

    # every node point to the next node
    # we can go from one node to the next using a process called traversal

    #  a method to check whether the head is empty or not
    def is_empty(self):
        return self.head == None  

    # Getting the size of the list
    def size(self):
        # we get the size of the list via a linear runtime
        # counting from one node to another starting from the head
        current = self.head
        count = 0

        # a loop to go until there is no other node
        # i.e while current does not equal None
        while current:
            count+=1
            # assigning the next node in the ref to current
            current = current.next_node
            # when we get to the end node and call the next node, current will equal to none hence we terminate the loop
        return count  
     
    # Add Method (adds data into the linked List)
    # Defining a method to add data into our list
    # WAYS TO ADD DATA INTO A LIST
    # We can add nodes from the head of the list (most recent node,will be the head of the list and the first data will be the tail of the list: Prepend)
    # We can flip around(most recent tail, first will be the head: Append)
    # Linked lists are only effecient when data is added either from the tail or head and not inserted
    def add(self, data):
        # passing the data to create a node
        new_node = Node(data)
        # before setting the head of the node, we set the value of the next node to what is currently at the head(since its the first data, None will be the next node)
        new_node.next_node = self.head

        # Now setting the head of the node
        self.head = new_node

    # Search Method
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or None if not found
        Takes Linear Time O(n)
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None


    # Inserting an item into the Linked List
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes constant time O(1) time but finding the node at the insertion point takes Linear time O(n)
        Therefore takes an overall linear time
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = new.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            # Inserting the new node between previous and next
            prev_node.next_node = new
            new.next_node = next_node
    
    # Remove method
    def remove(self, key):
        """
        Removes Node data that matches the key
        Returns the Node or None if the Key doesn't exist
        This takes Linear Time O(n) because in the worst case scenario, we need to search the entire list
        """
         
        current = self.head
        previous = None

        found = False

        # Loop keeps iterating as long as current is not equal to None
        while current and not found:
            if current.data == key and current is self.head:
                found == True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    # Representing our linked list
    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return '--> '.join(nodes)
        # return nodes


# Creating an instance of node
# n1 = Node(10)
# n2 = Node(20)

# n1.next_node = n2

# print(n1)
# print(n1.next_node)
# print(n2)

# # Getting the size of a linked list
# l = LinkedList()
# n1 = Node(10)

# # assinging n1 to the head of the linked list
# l.head = n1

# # Getting the size 
# print(l.size())

# Checking if the linked list works after adding data

l = LinkedList()

l.add(10)
l.add(2)
l.add(45)
l.add(15)

# Searching for 45
n = l.search(45)
print(n)
print(l)
# print(l.size())

# # printing the linked list
# print(l)