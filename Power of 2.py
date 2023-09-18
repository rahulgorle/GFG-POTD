class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        if n <= 0:
            return False
        
        # Count the number of set bits
        set_bits = 0
        while n:
            set_bits += n & 1
            n >>= 1
        
        return set_bits == 1
