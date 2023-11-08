class Solution:
    # Function to return a list of integers visited in the snake pattern in the matrix.
    def snakePattern(self, matrix):
        n = len(matrix)
        result = []

        for i in range(n):
            # If the current row is even, traverse from left to right.
            if i % 2 == 0:
                for j in range(n):
                    result.append(matrix[i][j])
            else:
                # If the current row is odd, traverse from right to left.
                for j in range(n - 1, -1, -1):
                    result.append(matrix[i][j])

        return result
