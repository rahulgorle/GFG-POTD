class Solution:
    def isLucky(self, n): 
        # Determine if a number is lucky or not
        divisor = 2
        while divisor <= n:
            if n % divisor == 0:
                return 0  # Not a lucky number
            n -= n // divisor
            divisor += 1
        return 1  # It's a lucky number
