class Solution:
    def isPossible(self, N, arr):
        # Calculate the total sum of all the digits in the array
        total_sum = sum(sum(map(int, str(x))) for x in arr)

        # If the total sum is divisible by 3, return 1; otherwise, return 0
        return 1 if total_sum % 3 == 0 else 0
