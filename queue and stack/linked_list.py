'''
Linked List has 2 parts : A node that stores the data and a pointer to the next Node.
So it is handled in 2 classes:

1. Node class with operations:

    1. init function to get the data and next node value
    2. get_data function to get the data of the node
    3. set_data function to set the data of the node
    4. get_next and set_function is again similar to the data function ; it would be to get and set the next node value respectively.
    5. has_next fucntion returns a Boolean whether the node has a next pointer or not

2. Linked List class with operations:

    1. init function to initilise the nodes
    2. get_size to return the size of the Linked List
    3. add function to add a node
    4. remove function to remove a node
    5. print_list to print the linked list
    6. sort to sort the linked list
    7. find function to find a item in a linked list
'''


class Node(object):

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def get_next(self):
        ''' get the next node value'''
        return self.nextNode

    def set_next(self, nextNode):
        ''' point the node to next node'''
        self.nextNode = nextNode

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def has_next(self):

        if self.nextNode == None:
            return False

        else:
            return True


class LinkedList(object):

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return f"Size of the Linked List is : {self.size}"

    def add(self, data):

        newNode = Node(data, self.root)
        self.root = newNode
        self.size += 1

    def remove(self, data):

        r_node = self.root
        prev_node = None

        while r_node:

            if r_node.get_data() == data:

                if prev_node:
                    prev_node.set_next(r_node.get_next())
                else:
                    self.root = r_node.get_next()
                self.size -= 1
                return True

            else:
                prev_node = r_node
                r_node = r_node.get_next()

        return False  # item not found

    def find(self, data):

        find_data = self.root

        while find_data:

            if find_data.get_data() == data:
                return f"Data found {data}"

            elif find_data.get_next() == None:
                return False  # item not in list

            else:
                find_data = find_data.get_next()

        return None

    def print_list(self):
        pass

    def sort_list():

        pass


linked = LinkedList()

linked.add(4)
linked.add(5)
linked.add(7)
linked.add(1)

print(linked.get_size())

print(str(linked.find(5)))

linked.add(9)
linked.add(0)

print(linked.get_size())
print(linked.find(0))

print(linked.remove(4))
print(linked.get_size())
print(linked.find(4))
