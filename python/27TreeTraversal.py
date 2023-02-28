# Tree Traversal in Python
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

    
def inorder(root):
    if root:
        # Traverse Left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)

def postorder(root):
    if root:
        # Traverse Left
        postorder(root.left)
        # Traverse right 
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')


def preorder(root):
    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal")
inorder(root)

print("\nPreorder Traversal")
preorder(root)

print("\nPostorder Traversal")
postorder(root)

