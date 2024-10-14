class Solution:
    def getCount(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
