# IMPLEMENTATION OF A QUEUE
class Queue:

    # instatiating the queue class
    def __init__(self):
        self.queue = []

    # Adding an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None 
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        print(self.queue)


    # size of the queue
    def size(self):
        print (len(self.queue))


# Creating an object of the class
q = Queue()

# adding elements into the queue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

# printing the queue
q.display()
q.size()

# removing elements from the queue
q.dequeue()
q.dequeue()

q.display()
q.size()



