# DEQUEUE IMPLEMENTATION

class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


d = Dequeue()
print(d.isEmpty())

d.addRear(8)
d.addRear(5)
d.addRear(7)
d.addRear(6)
d.addRear(2)
d.addFront(4)
d.addFront(12)
print(d.items)

print(d.size())
print(d.isEmpty())

d.addRear(11)
print(d.removeRear())
print(d.removeFront())

d.addFront(55)
d.addRear(45)

print(d.items)
