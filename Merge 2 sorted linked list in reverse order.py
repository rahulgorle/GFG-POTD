class Solution:
    def mergeResult(self, head1, head2):
        dummy = Node(0)
        
        while head1 and head2:
            if head1.data < head2.data:
                newhead, head1 = head1, head1.next
            else:
                newhead, head2 = head2, head2.next
            newhead.next, dummy.next = dummy.next, newhead
        
        head = head1 if head1 else head2
        
        while head:
            newhead, head = head, head.next
            newhead.next, dummy.next = dummy.next, newhead
        return dummy.next
