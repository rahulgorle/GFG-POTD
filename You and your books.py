class Solution:
    def max_Books(self, n, k, arr):
        res, count = 0, 0
        for i in range(n):
            count = count+arr[i] if arr[i]<=k else 0
            res = max(res, count)
        return res
