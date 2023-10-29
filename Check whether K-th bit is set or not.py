class Solution:
    
    # Function to check if Kth bit is set or not.
    def checkKthBit(self, n, k):
        # Left shift 1 by k positions and perform bitwise AND with n
        # If the kth bit is set, the result will be non-zero
        return (n & (1 << k)) != 0
