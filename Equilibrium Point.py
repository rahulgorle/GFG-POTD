class Solution:
    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        # Calculate the total sum of the array.
        total_sum = sum(A)
        left_sum = 0
        
        for i in range(N):
            # Subtract the current element from the total sum.
            total_sum -= A[i]
            
            # If the left sum equals the remaining total sum, it's an equilibrium point.
            if left_sum == total_sum:
                return i + 1  # 1-based indexing
                
            # Add the current element to the left sum for the next iteration.
            left_sum += A[i]
        
        # If no equilibrium point is found, return -1.
        return -1
