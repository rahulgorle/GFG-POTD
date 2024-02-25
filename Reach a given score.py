#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        # Initialize a dp array to store the number of ways to reach each score from 0 to n
        dp = [0] * (n + 1)
        
        # There is one way to reach score 0 (by not choosing any move)
        dp[0] = 1
        
        # Iterate through each possible move (3, 5, 10)
        for move in [3, 5, 10]:
            # Update dp array for scores achievable with the current move
            for score in range(move, n + 1):
                dp[score] += dp[score - move]
        
        # Return the number of ways to reach the desired score n
        return dp[n]
        
