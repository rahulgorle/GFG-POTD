class Solution:
    
    def missingNumber(self, n, arr):
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum
