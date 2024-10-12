class Solution:
    def pairWithMaxSum(self, arr):
        if len(arr) < 2:
            return -1 
        m = 0
        for i in range(len(arr) - 1):
            m = max(m, arr[i] + arr[i + 1])
        return m
