class Solution:
    # Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self, matrix, n):
        upper_sum = 0
        lower_sum = 0

        for i in range(n):
            for j in range(i, n):
                upper_sum += matrix[i][j]
                lower_sum += matrix[j][i]

        return [upper_sum, lower_sum]
