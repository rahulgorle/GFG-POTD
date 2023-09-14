class Solution:
    def perfectSum(self, numbers, length, targetSum):
        dp = [1] + [0] * targetSum
        MOD = 10**9 + 7

        for num in numbers:
            for currSum in range(targetSum, num - 1, -1):
                dp[currSum] = (dp[currSum] + dp[currSum - num]) % MOD
        
        return dp[targetSum]
