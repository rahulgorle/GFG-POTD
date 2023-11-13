class Solution:
    
    # Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        # Create a 2D table to store the length of the
        # shortest common supersequence of prefixes X and Y.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table in a bottom-up manner.
        for i in range(m + 1):
            for j in range(n + 1):
                # If one of the strings is empty, the length of the
                # supersequence is the length of the other string.
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                # If the last characters match, extend the supersequence
                # by one character and consider the rest of both strings.
                elif X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                # If the last characters do not match, take the minimum
                # of two possibilities: append the last character of X
                # and consider the rest of Y, or append the last character
                # of Y and consider the rest of X.
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the shortest common supersequence is given
        # by the bottom-right cell of the table.
        return dp[m][n]
