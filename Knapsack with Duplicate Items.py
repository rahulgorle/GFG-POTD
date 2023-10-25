class Solution:
    def knapSack(self, N, W, val, wt):
        # Initialize a list to store the maximum value for each weight from 0 to W
        dp = [0] * (W + 1)
        
        # Iterate through each item
        for i in range(N):
            # Update dp for each weight from wt[i] to W
            for w in range(wt[i], W + 1):
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
        
        # The maximum value for the knapsack with weight limit W is stored in dp[W]
        return dp[W]
