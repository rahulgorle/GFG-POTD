class Solution:
    def countWays(self,n, k):
        MOD = 1000000007
        
        # If there are no posts, there is 0 way to paint the fence.
        if n == 0:
            return 0
        
        # If there is only one post, there are k ways to paint it.
        if n == 1:
            return k
        
        # Initialize the dp array with 0 for 0 and 1 post.
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        
        # Fill the dp array using the recurrence relation.
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)) % MOD
        
        return dp[n]
