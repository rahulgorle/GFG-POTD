class Solution:
    def sumOfDivisors(self, N):
        total_sum = 0
        for i in range(1, N + 1):
            total_sum += i * (N // i)
        return total_sum
