
# CIRCULAR QUEUE IMPLEMENTATION
class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1
        # set to -1 to be outside the indexes


    # Insert an element into the circular queue
    def enqueue(self, data):
        # self.tail(index of tail + 1 to make it the length of the queue % k (length of queue) = 0 (index of head))
        if((self.tail + 1) % self.k == self.head):

            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head == 0
            self.tail == 0
            self.queue[self.tail] = data 

        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from a circular queue
    def dequeue(self):
        if(self.head == -1):
            print("The Circular Queue is Empty\n")
        
        # when only one element is left in the queue
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printQueue(self):
        if(self.head == -1):
            print("No Element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()



# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printQueue()



