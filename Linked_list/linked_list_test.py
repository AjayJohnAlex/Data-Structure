class Node(object):
    
    def __init__(self,data=None):
        self.data = data
        self.next_node = None
        
    def __repr__(self):
        return f"Node data is : {self.data} "


class LinkedList(object):
    
    def __init__(self):
        self.head = None
               
    def addNode(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def searchNode(self, search_data):
        
        current_node = self.head
        
        while current_node:
            if search_data == current_node.data:
                return f"Node is present in the list :{self.head}"
            else:
                current_node = current_node.next_node
        return "node not in Linked list"
        
    def __repr__(self):
        
        current_linked_list  = []
        current_head = self.head
        while current_head:
            current_linked_list.append(str(current_head.data))
            
            current_head = current_head.next_node
            
        return '->'.join(current_linked_list)
    
ll = LinkedList()
ll.addNode(10)
print(ll.head)
ll.addNode(20)
print(ll.head)
ll.addNode(40)
print(ll.head)
print(ll)
print(ll.searchNode(10))
print(ll.searchNode(220))