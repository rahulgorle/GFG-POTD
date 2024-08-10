class Solution:

    def rotate(self, head, k):
        
        temp  = head
        
        while temp and temp.next:
            temp=temp.next
        
        for i in range(k):
            t = head
            head=head.next
            t.next=None
            temp.next=t
            temp=temp.next
        
        return head
