from typing import List

class Solution:
    def sumOfPowers(self, start: int, end: int) -> int:
        # Create a list to store the smallest prime factor for each number in the range
        smallest_prime_factor = [i for i in range(end + 1)]

        # Sieve of Eratosthenes to find the smallest prime factor for each number
        for i in range(2, int(end**0.5) + 1):
            if smallest_prime_factor[i] == i:
                smallest_prime_factor[i*i:end+1:i] = [i] * len(smallest_prime_factor[i*i:end+1:i])

        distinct_prime_factors_count = 0

        # Count distinct prime factors for each number in the given range
        for num in range(start, end + 1):
            while num > 1:
                distinct_prime_factors_count += 1
                num //= smallest_prime_factor[num]

        return distinct_prime_factors_count
