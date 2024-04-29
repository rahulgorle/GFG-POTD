class Solution:
    def deleteK(self, head, k):
        dummy = node(0)
        dummy.next = head
        n, w = 0, dummy
        while w:
            n = (n+1)%k
            if n == 0 and w.next:
                w.next = w.next.next
            else:
                w = w.next
        return dummy.next
