class Solution:
    def minimumStep(self, n):
        count = 0  # To store the minimum number of steps

        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
            count += 1

        return count
