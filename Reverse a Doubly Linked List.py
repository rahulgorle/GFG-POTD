class Solution:
    def reverseDLL(self, head):
        curr = head
        while curr:
            # Swap the prev and next pointers
            curr.next, curr.prev = curr.prev, curr.next
            # Move to the next node
            head = curr
            curr = curr.prev
            
        # The last node (which was the head) is now the new head
        return head
