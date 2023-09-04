class Solution:
    def fill(self, n, m, matrix):
        if not matrix:
            return matrix

        # Helper function to perform DFS starting from a given cell.
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or matrix[r][c] != 'O':
                return

            matrix[r][c] = 'V'  # Mark the cell as visited

            # Explore neighboring cells
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Identify and mark all 'O' cells on the boundary as 'V'.
        for i in range(n):
            if matrix[i][0] == 'O':
                dfs(i, 0)
            if matrix[i][m - 1] == 'O':
                dfs(i, m - 1)
        for j in range(m):
            if matrix[0][j] == 'O':
                dfs(0, j)
            if matrix[n - 1][j] == 'O':
                dfs(n - 1, j)

        # Step 2: Mark any remaining unvisited 'O' cells as 'X' and restore 'V' to 'O'.
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 'O':
                    matrix[i][j] = 'X'
                elif matrix[i][j] == 'V':
                    matrix[i][j] = 'O'

        return matrix
