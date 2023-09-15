class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)
        
        # If the total sum is odd, it's not possible to partition into two equal parts
        if total_sum % 2 != 0:
            return 0
        
        target_sum = total_sum // 2
        dp = [[False] * (target_sum + 1) for _ in range(N + 1)]
        
        for i in range(N + 1):
            dp[i][0] = True
        
        for i in range(1, N + 1):
            for j in range(1, target_sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return 1 if dp[N][target_sum] else 0
