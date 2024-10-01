class Solution:
    def multiply_two_lists(self, first, second):
        fir = 0
        sec = 0
        cur = first
        cur1 = second
        while(cur):
            fir = (cur.data + (fir * 10))
            cur = cur.next
        while(cur1):
            sec = (cur1.data + (sec * 10))
            cur1 = cur1.next
        ans = (fir * sec) % 1000000007
        return ans
