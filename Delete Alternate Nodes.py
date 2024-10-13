class Solution:
    def deleteAlt(self, cur):
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return cur
