class Solution:
    def isPalindrome(self, head):
        ans = []
        while head :
            ans.append(head.data)
            head = head.next
        
        return ans == ans[::-1]
