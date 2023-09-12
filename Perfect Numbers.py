import math

class Solution:
    def isPerfectNumber(self, N):
        if N <= 1:
            return 0
        
        # Initialize the sum of factors
        factors_sum = 1  # 1 is always a factor
        
        # Iterate through numbers from 2 to the square root of N
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                factors_sum += i  # Add the factor
                if i != N // i:  # If it's not a perfect square, add the other factor
                    factors_sum += N // i
        
        # Check if the sum of factors is equal to N
        if factors_sum == N:
            return 1
        else:
            return 0
