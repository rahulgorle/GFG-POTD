class Solution:
    def gameOfXor(self, N , A):
        # code here 
        res = 0
        for i in range(N):
            if ((i + 1) & 1) and ((N - i) & 1):
                res = (res ^ A[i])
        return res
