class Solution:
    def alternatingSplitList(self, head):
        if head is None:
            return [None, None]
        if head and head.next is None:
            return [head, None]
        h1 = head
        h2 = head.next
        temp1 = h1
        temp2 = h2
        
        while temp1 and temp2:
            temp1.next = temp2.next
            temp1 = temp1.next
            
            if temp1:
                temp2.next = temp1.next
                temp2 = temp2.next

        return [h1, h2]
