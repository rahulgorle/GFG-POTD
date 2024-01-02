class Solution():
    def maxSumWithK(self, a, n, k):
        maxend = 0
        s = 0
        res = float('-inf')
        for i in range(n):
            s += a[i]
            if i >= k:
                s -= a[i - k]
                maxend = max(0, a[i - k], a[i - k] + maxend)
            if i >= k - 1:
                res = max(res, s + maxend)
        return res
