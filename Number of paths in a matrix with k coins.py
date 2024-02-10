class Solution:
    def numberOfPath(self, n, k, arr):
        def count_paths(i, j, n, k, arr, dp):
            # If we reached the bottom-right cell and the sum matches k, return 1 (one valid path found)
            if i == n - 1 and j == n - 1 and k == arr[i][j]:
                return 1
            # If out of bounds or the remaining sum is negative, return 0 (no valid path)
            if i >= n or j >= n or k < 0:
                return 0
            # If the result for the current cell and sum is already computed, return it
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            # Explore downward and rightward paths, updating the DP table with the sum counts
            down = count_paths(i + 1, j, n, k - arr[i][j], arr, dp)
            right = count_paths(i, j + 1, n, k - arr[i][j], arr, dp)
            # Update DP table with the count of paths reaching the current cell with the current sum
            dp[i][j][k] = down + right
            return dp[i][j][k]
        
        # Initialize DP table with -1 values
        dp = [[[-1 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)] 
        # Start the recursive function from the top-left cell
        return count_paths(0, 0, n, k, arr, dp)
