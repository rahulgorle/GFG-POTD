class Solution:
    def delete_node(self, head, x):
        if x == 1:
            head.next.prev == None
            return head.next
            
        cnt = 1
        temp = head
        while cnt < x - 1:
            temp = temp.next
            cnt += 1
        temp.next = temp.next.next
        return head
