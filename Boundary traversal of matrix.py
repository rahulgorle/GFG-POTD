class Solution:
    def BoundaryTraversal(self, matrix, n, m):
        result = []

        if n == 1:  # Only one row
            return matrix[0]

        if m == 1:  # Only one column
            return [matrix[i][0] for i in range(n)]

        for i in range(m):
            result.append(matrix[0][i])  # Traverse the first row

        for i in range(1, n):
            result.append(matrix[i][m - 1])  # Traverse the last column

        if n > 1:
            for i in range(m - 2, -1, -1):
                result.append(matrix[n - 1][i])  # Traverse the last row

        if m > 1:
            for i in range(n - 2, 0, -1):
                result.append(matrix[i][0])  # Traverse the first column

        return result
