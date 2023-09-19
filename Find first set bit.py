class Solution:
    
    # Function to find position of first set bit in the given number.
    def getFirstSetBit(self, n):
        if n == 0:
            return 0
        
        position = 1
        # Find the rightmost set bit by shifting the number to the right
        # until it becomes 1 (indicating the rightmost set bit).
        while (n & 1) == 0:
            n >>= 1
            position += 1
        
        return position
