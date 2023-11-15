class Solution:
    def betterString(self, str1, str2):
        mod = 10**9 + 7
        
        # Function to calculate the number of distinct subsequences
        def countDistinctSubsequences(s):
            n = len(s)
            last_occurrence = [-1] * 256
            dp = [0] * (n + 1)
            dp[0] = 1  # Empty string has one subsequence

            for i in range(1, n + 1):
                dp[i] = (2 * dp[i - 1]) % mod

                if last_occurrence[ord(s[i - 1])] != -1:
                    dp[i] = (dp[i] - dp[last_occurrence[ord(s[i - 1])]]) % mod

                last_occurrence[ord(s[i - 1])] = i - 1

            return dp[n]

        # Count distinct subsequences for both strings
        count_str1 = countDistinctSubsequences(str1)
        count_str2 = countDistinctSubsequences(str2)

        # Return the better string
        return str1 if count_str1 >= count_str2 else str2
