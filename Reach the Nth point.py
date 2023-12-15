#User function Template for python3

class Solution:
    def nthPoint(self,n):
        if n==1:
            return 1
        mod=10**9+7
        prev=1
        cur=2
        for i in range(3,n+1):
            val=(prev+cur)%mod
            prev=cur
            cur=val
        return cur
