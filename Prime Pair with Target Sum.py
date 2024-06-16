from typing import List

class Solution:
    def getPrimes(self, n : int) -> List[int]:
        primes = [True] * (n + 1)
        result = []

        primes[0] = primes[1] = False

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        found = False
        for i in range(2, n + 1):
            if primes[i] and primes[n - i]:
                result.append(i)
                result.append(n - i)
                found = True
                break

        if not found:
            result.extend([-1, -1])

        return result
