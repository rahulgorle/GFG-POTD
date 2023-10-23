class Solution:
    def maxSumIS(self, Arr, n):
        dp = [0] * n  # Initialize the dp array with zeros

        for i in range(n):
            dp[i] = Arr[i]  # Initialize each element as the corresponding element in the input array

        for i in range(1, n):
            for j in range(i):
                if Arr[i] > Arr[j]:
                    dp[i] = max(dp[i], dp[j] + Arr[i])

        return max(dp)
