class Node:
    
    def __init__(self,data=None):
        '''Creates a node in the linked list
        Takes a data and next_node(pointer to next node )'''
        self.data = data
        self.next_node = None
        
    def __repr__(self):
        
        return  f"<NODE data is: {self.data} "
    

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def size(self):
        '''Return the no of nodes in a linked list and takes O(n) time'''
        
        current_node = self.head
        count = 0
        while current_node :
            
            current_node = self.next_node
            count +=1
            
        return count
    
    def add(self, data):
        '''Adding a new node/item to the linked list:
        Create a node -> assign new_node.next_node as current head -> assign head to new node
        Takes O(1) time'''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        '''Search for a key in the linked list.
        If not found in the list then return None else return data found
        takes O(n) time'''
        
        current_node = self.head
        while current_node:
            
            if key == current_node.data:
                return f"{current_node}>"
            else:
                current_node = current_node.next_node
        
        return "Item not in Linked List"
    
    
    def __repr__(self):
        '''Return string rep of list 
        takes O(n) time'''
        
        nodes = []
        current_node = self.head
        
        while current_node:
            if current_node == self.head:
                nodes.append(f"[START NODE: {current_node.data}]")
            elif current_node.next_node == None:
                nodes.append(f"[END NODE: {current_node.data}]")
            else:
                nodes.append(f"[ {current_node.data} ]")
            
            current_node = current_node.next_node
        
        return '->'.join(nodes)
    
    

ll = LinkedList()
ll.add(10)
print(ll.head)
ll.add(20)
print(ll.head)
ll.add(40)
print(ll.head)
print(ll)
print(ll.search(10))
print(ll.search(220))
