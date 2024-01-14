class Solution:
    def repeatedRows(self, matrix, num_rows, num_columns):
        unique_rows_set = set()
        repeated_rows_indices = []
       
        for i in range(num_rows):
            if tuple(matrix[i]) in unique_rows_set:
                repeated_rows_indices.append(i)
            else:
                unique_rows_set.add(tuple(matrix[i]))

        return repeated_rows_indices
