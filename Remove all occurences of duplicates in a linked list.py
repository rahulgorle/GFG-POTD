class Solution:
    def removeAllDuplicates(self, head):
        #code here
        # Create a dummy node that points to the head of the list
        dummy = Node(0)
        dummy.next = head
        # Initialize current node to dummy
        current = dummy
        while current.next and current.next.next:
            # If the current node's next two nodes have the same data, we have duplicates
            if current.next.data == current.next.next.data:
                # Store the duplicate value
                duplicate_value = current.next.data
                # Skip all nodes with the duplicate value
                while current.next and current.next.data == duplicate_value:
                    current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        return dummy.next
