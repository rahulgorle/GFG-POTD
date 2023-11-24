from math import factorial
class Solution:
    def nthRowOfPascalTriangle(self, row_number):
        pascal_row = [1] * row_number
        left_index, right_index = 1, row_number - 2
        numerator = factorial(row_number - 1)

        while left_index <= right_index:
            binomial_coefficient = numerator // (factorial(row_number - left_index - 1) * factorial(left_index))
            pascal_row[left_index] = pascal_row[right_index] = binomial_coefficient % (10**9 + 7)
            left_index, right_index = left_index + 1, right_index - 1

        return pascal_row
