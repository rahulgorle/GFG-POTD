class Solution:
    def maxGold(self, n, m, M):
        # code here
        if n==1:
            return sum(M[0])
        if m==1:
            return sum(list(zip(*M))[0])
        dp=[[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            dp[i][m-1]=M[i][m-1]
        for j in range(m-2,-1,-1):
            dp[0][j]=M[0][j]+max(dp[0][j+1],dp[1][j+1])
            for i in range(1,n-1):
                dp[i][j]=M[i][j]+max(max(dp[i-1][j+1],dp[i][j+1]),dp[i+1][j+1])
            dp[n-1][j]=M[n-1][j]+max(dp[n-2][j+1],dp[n-1][j+1])
        return max(list(zip(*dp))[0])
