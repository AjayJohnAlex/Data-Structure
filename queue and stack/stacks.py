class Stack(object):

    def __init__(self):

        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


S = Stack()

print(S.isEmpty())
S.push(1)
S.push("QWERTY")
S.push(True)
print(S.peek())
S.push(False)
S.push(11)
print(S.size())
S.pop()
print(S.size())
