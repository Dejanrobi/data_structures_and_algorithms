# Stack Implementation in python

# Creating a stack
def create_stack():
    stack=[]
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into a stack
def push(stack, item):
    stack.append(item)
    print("Pushed item: ", item)


# Removing an element from the stack
def pop(stack):
    if(check_empty(stack)):
        return "Stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))

# Printing the popped item
print("Popped item: " + pop(stack))
print("Popped item: " + pop(stack))
print("Popped item: " + pop(stack))

# Stack after popping an element
print(str(stack))
