class Solution:
    # Function to return list containing first n Fibonacci numbers.
    def printFibb(self, n):
        fib_numbers = []
        a, b = 1, 1
        for i in range(n):
            fib_numbers.append(a)
            a, b = b, a + b
        return fib_numbers
