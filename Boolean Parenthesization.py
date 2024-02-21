#User function Template for python3

class Solution:
    def countWays(self, n, s):
        MOD = 1003
        # Function to evaluate if expression between i and j (inclusive) evaluates to true and false
        def evaluate(i, j):
            if i == j:
                return (1 if s[i] == 'T' else 0), (1 if s[i] == 'F' else 0)
            true_count, false_count = 0, 0
            for k in range(i+1, j, 2):
                left_true, left_false = dp[i][k-1]
                right_true, right_false = dp[k+1][j]
                if s[k] == '&':
                    true_count += (left_true * right_true) % MOD
                    false_count += ((left_true * right_false) + (left_false * right_true) + (left_false * right_false)) % MOD
                elif s[k] == '|':
                    true_count += ((left_true * right_false) + (left_false * right_true) + (left_true * right_true)) % MOD
                    false_count += (left_false * right_false) % MOD
                elif s[k] == '^':
                    true_count += ((left_true * right_false) + (left_false * right_true)) % MOD
                    false_count += ((left_true * right_true) + (left_false * right_false)) % MOD
            return true_count % MOD, false_count % MOD

        # dp[i][j] represents the number of ways to parenthesize subexpression s[i:j+1]
        dp = [[(0, 0) for _ in range(n)] for _ in range(n)]

        # Fill the diagonal elements
        for i in range(n):
            if s[i] == 'T':
                dp[i][i] = (1, 0)
            else:
                dp[i][i] = (0, 1)

        # Fill the dp table diagonally
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                dp[i][j] = evaluate(i, j)

        return dp[0][n-1][0]
