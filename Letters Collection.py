class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        # code here
        ans = []
        it = [-1,+1]
        for d,r,c in queries:
            Sum = 0
            for i in it:
                for col in range(c-d+1,c+d):
                    row = r+i*d
                    if row>=0 and row<n and col>=0 and col<m:
                        Sum+=mat[row][col]
            for i in it:
                for row in range(r-d,r+d+1):
                    col = c+i*d
                    if row>=0 and row<n and col>=0 and col<m:
                        Sum+=mat[row][col]
                    
            ans.append(Sum)
        return ans
