class Solution:
    def distinctSubsequences(self, S):
        MOD = 10**9 + 7
        n = len(S)
        
        # Initialize a DP array to store the count of distinct subsequences
        dp = [0] * (n + 1)
        
        # An empty subsequence is always present
        dp[0] = 1
        
        # Create a dictionary to store the last index of each character
        last_seen = {}
        
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % MOD  # Doubling the count
            
            # If the current character has been seen before, subtract the count of subsequences
            if S[i - 1] in last_seen:
                dp[i] = (dp[i] - dp[last_seen[S[i - 1]] - 1] + MOD) % MOD
            
            # Update the last seen index of the current character
            last_seen[S[i - 1]] = i
        
        return dp[n]
