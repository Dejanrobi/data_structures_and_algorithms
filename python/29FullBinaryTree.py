# Checking if a binary Tree is a Full Binary Tree
# Creating a node
class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None


# Checking full binary tree
def isFullTree(root):
    # stopping condition for an empty tree
    # Tree empty case
    if root is None:
        return True
    
    # stoping condition if there are no other nodes
    # Checking whether the child is present (this returns true if the children are not their in both nodes)
    if root.leftChild is None and root.rightChild is None:
        return True
    
    # if the left child and the right child is present it calls the entire function again
    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))
    
    return False


root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.rightChild.leftChild = Node(6)
root.leftChild.rightChild.rightChild = Node(7)

if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")