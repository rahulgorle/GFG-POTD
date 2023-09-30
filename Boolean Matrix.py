def booleanMatrix(matrix):
    R = len(matrix)
    C = len(matrix[0])

    # Initialize row_flag and col_flag arrays
    row_flag = [0] * R
    col_flag = [0] * C

    # Mark rows and columns to be modified
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1:
                row_flag[i] = 1
                col_flag[j] = 1

    # Modify the matrix based on row_flag and col_flag
    for i in range(R):
        for j in range(C):
            if row_flag[i] == 1 or col_flag[j] == 1:
                matrix[i][j] = 1
