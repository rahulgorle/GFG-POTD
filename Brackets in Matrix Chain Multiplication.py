class Solution:
    def matrixChainOrder(self, p, n):
        # Create a 2D table to store the minimum number of multiplications
        # and the position to split the chain for optimal parenthesization
        dp = [[0] * n for _ in range(n)]
        split = [[''] * n for _ in range(n)]

        # Fill the dp table using bottom-up dynamic programming
        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')  # Initialize with infinity

                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        split[i][j] = k

        # Build the optimal parenthesization string
        return self.constructParenthesis(split, 1, n - 1)

    def constructParenthesis(self, split, i, j):
        if i == j:
            return chr(ord('A') + i - 1)
        else:
            left = self.constructParenthesis(split, i, split[i][j])
            right = self.constructParenthesis(split, split[i][j] + 1, j)
            return '({}{})'.format(left, right)

