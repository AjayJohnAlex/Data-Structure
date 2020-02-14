'''
1. Max Heap is a binary tree except the bottom layer  which should be filled from left to right
2. Every node must be less than or equal to the parentt node
3. Max Heap is very fast
    1. Insert is O(logn) Push
    2. Get Max in O(1) Peek
    3. Remove Max in O(log n) Pop
4. Easy to implement in an array :

---------------------------------------------------
|  1  | 2   |  3 |  4 | 5  | 6  | 7  | 8  | 9 | 10 | --> index
----------------------------------------------------
|  25 | 16  | 24 | 5  | 11 | 19 | 1  | 2  | 3 | 5  | --> value
----------------------------------------------------
    if eg : for arr[4] = 5
        the parent[4] = 4/2 = 2 -> p[2]
        the left child  = 4*2 =8 -> p[8]
        the right child = 4*2 + 1 -> p[9]
5. Easiest way to add a value is add in the end and float it up to the correct position. Same goes for Pop with the diff being that the max value is pop and stored till the new heap is build.
'''


class MaxHeap:

    def __init__(self, items=[]):

        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        ''' 3 situations:
                If there are more than 2 values in a heap
                If there are exactly 2 values and
                If the heap is empty
        '''
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)

        elif len(self.heap) == 2:
            max = self.heap.pop()

        else:
            return False

    def __swap(self, i, j):
        '''
        Swap , Bubble Down and FloatUp are internal functions
        '''

        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        '''
        If the index = 1 then no floating to be done ;
        else float to top
        '''

        parent = index // 2
        if index <= 1:
            return

        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):

        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)


h = MaxHeap([95, 3, 21])
print(str(h.heap[0:len(h.heap)]))
h.push(10)
print(str(h.heap[0:len(h.heap)]))
h.pop()
print(str(h.heap[0:len(h.heap)]))
