class Solution:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def minNumber(self, arr, n):
        # Calculate the sum of the array
        arr_sum = sum(arr)

        # Check if the sum is a prime number
        if self.is_prime(arr_sum):
            return 0

        # Find the smallest positive number to make the sum prime
        for i in range(1, arr_sum):
            if self.is_prime(arr_sum + i):
                return i
