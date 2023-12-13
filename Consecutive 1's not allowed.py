class Solution:
    def countStrings(self, n):
        # Modulo constant for result
        modulo = 10**9 + 7

        # Initial values for Fibonacci sequence
        fib_prev, fib_current = 1, 2

        # Calculate Fibonacci sequence iteratively
        for i in range(2, n + 1):
            fib_prev, fib_current = fib_current, (fib_prev + fib_current) % modulo

        # Return the result for the given length n
        return fib_current
