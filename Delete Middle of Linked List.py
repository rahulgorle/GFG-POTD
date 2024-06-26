class Solution:
    def deleteMid(self,head):
        if head.next is None:
            return None
        fast=slow=head
        while fast and fast.next and fast.next.next and fast.next.next.next:
            fast=fast.next.next
            slow=slow.next
        slow.next=slow.next.next
        return head
