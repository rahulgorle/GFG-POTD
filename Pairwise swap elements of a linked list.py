# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class definition
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# Solution class definition
class Solution:
    def pairWiseSwap(self, head):
        if not head or not head.next:
            return head
        
        prev = None
        current = head
        
        while current and current.next:
            next_node = current.next
            current.next = next_node.next
            next_node.next = current
            
            if prev:
                prev.next = next_node
            else:
                head = next_node
            
            prev = current
            current = current.next
        
        return head
