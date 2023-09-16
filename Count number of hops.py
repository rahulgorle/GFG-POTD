class Solution:
    # Function to count the number of ways in which frog can reach the top.
    def countWays(self, n):
        MOD = 1000000007
        # Initialize a list to store the number of ways to reach each step.
        dp = [0] * (n + 1)
        
        # There is 1 way to reach step 0 (base case).
        dp[0] = 1
        
        for i in range(1, n + 1):
            # Try jumping 1, 2, and 3 steps and update the number of ways.
            for j in range(1, 4):
                if i - j >= 0:
                    dp[i] = (dp[i] + dp[i - j]) % MOD
        
        return dp[n]
