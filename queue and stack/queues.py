class Queues(object):

    def __init__(self):

        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dqueue(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


Q = Queues()

print(Q.isEmpty())
Q.enqueue(1)
Q.enqueue("QWERTY")
Q.enqueue(True)
print(Q.peek())
Q.enqueue(False)
Q.enqueue(11)
print(Q.size())
Q.dqueue()
print(Q.size())
