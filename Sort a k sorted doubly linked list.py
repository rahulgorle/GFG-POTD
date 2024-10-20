from heapq import heappush, heappop
class Solution:
    def sortAKSortedDLL(self, head, k):
        p = q = head
        h = []
        while q:
            heappush(h, q.data)
            if len(h) >= k + 1:
                p.data = heappop(h)
                p = p.next
            q = q.next
        while h:
            p.data = heappop(h)
            p = p.next
        return head
