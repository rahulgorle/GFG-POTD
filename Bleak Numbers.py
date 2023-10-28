from math import log2

class Solution:
    def is_bleak(self, n):
        bits = int(log2(n)) + 1

        for x in range(n - bits, n + 1):
            sum_bits = x + bin(x).count('1')
           
            if sum_bits == n:
                return 0

        return 1
