class Solution:
    def sumMatrix(self, n, q):
        lower_bound = max(1, q - n)
        upper_bound = min(n, q - 1)
        
        if lower_bound > upper_bound:
            return 0
            
        return upper_bound - lower_bound + 1
