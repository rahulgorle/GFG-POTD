class Solution:
    def antiDiagonalPattern(self, matrix):
        num_rows, num_cols = len(matrix), len(matrix[0])
        anti_diagonal_groups = {}

        for i in range(num_rows):
            for j in range(num_cols):
                anti_diagonal_groups.setdefault(i + j, []).append(matrix[i][j])

        return [element for group in anti_diagonal_groups.values() for element in group]
