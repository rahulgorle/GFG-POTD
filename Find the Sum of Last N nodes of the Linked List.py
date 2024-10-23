class Solution:
    def sumOfLastN_Nodes(self, head, n):
        total = 0
        curr = head
        count = 0
        while curr:
            total += curr.data
            curr = curr.next
            count += 1
        curr = head
        count -= n
        while count:
            total -= curr.data
            curr = curr.next
            count -= 1
        return total
