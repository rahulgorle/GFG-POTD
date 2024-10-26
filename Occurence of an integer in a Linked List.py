class Solution:
    def count(self, head, key):
        ans = 0
        temp = head
        while temp:
            if temp.data == key:
                ans += 1
            temp = temp.next
        return ans
