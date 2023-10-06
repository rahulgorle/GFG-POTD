class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def rearrange(self, head):
        if head is None or head.next is None or head.next.next is None:
            return
        
        # Separate the original list and the alternative nodes list
        original_head = head
        alternative_head = head.next
        original_current = original_head
        alternative_current = alternative_head
        
        while alternative_current is not None and alternative_current.next is not None:
            original_current.next = alternative_current.next
            original_current = original_current.next
            alternative_current.next = original_current.next
            alternative_current = alternative_current.next
        
        original_current.next = None
        
        # Reverse the alternative nodes list
        alternative_head = self.reverse(alternative_head)
        
        # Append the reversed alternative list to the end of the original list
        original_current = original_head
        while original_current.next is not None:
            original_current = original_current.next
        original_current.next = alternative_head
