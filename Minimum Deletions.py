class Solution:
    def minimumNumberOfDeletions(self, S):
        n = len(S)
        dp = [[0] * n for _ in range(n)]

        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
