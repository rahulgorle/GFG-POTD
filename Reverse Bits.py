class Solution:
    def reversedBits(self, n):
        res = 0
        for i in range(0, 32):
            res = res << 1
            bit = n % 2
            res += bit
            n = n >> 1
        return res
