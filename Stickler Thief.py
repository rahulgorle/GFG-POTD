class Solution:
    
    # Function to find the maximum money the thief can get.
    def FindMaxSum(self, a, n):
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        
        # Create a list to store the maximum money that can be obtained
        # if the thief starts from each house.
        dp = [0] * n
        
        # Initialize the first two values of dp.
        dp[0] = a[0]
        dp[1] = max(a[0], a[1])
        
        for i in range(2, n):
            # The thief has two choices: either loot the current house
            # or skip it and take the maximum from the previous house.
            dp[i] = max(dp[i-1], dp[i-2] + a[i])
        
        # The maximum money the thief can get will be in the last house.
        return dp[n-1]
