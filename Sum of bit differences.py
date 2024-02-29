class Solution:
    def sumBitDifferences(self, arr, n):
        ans = 0
        for i in range(32):
            count_ones = 0
            for j in arr:
                if j & (1 << i):
                    count_ones += 1
            count_zeros = n - count_ones
            ans += count_ones * count_zeros
        return 2 * ans
