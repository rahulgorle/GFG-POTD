class Solution:    
    def countX(self, L, R, X):
        count = 0

        # Loop through each number in the range (L+1, R)
        for num in range(L+1, R):
            # Count the occurrences of X in the current number
            count += str(num).count(str(X))

        return count
