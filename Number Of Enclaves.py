from typing import List

class Solution:
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(row, col):
            queue = [(row, col)]
            grid[row][col] = 0  # Mark the cell as visited

            while queue:
                r, c = queue.pop(0)

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] = 0  # Mark the cell as visited
                        queue.append((nr, nc))

        n, m = len(grid), len(grid[0])

        # Mark land cells on the boundary
        for i in range(n):
            if grid[i][0] == 1:
                bfs(i, 0)
            if grid[i][m - 1] == 1:
                bfs(i, m - 1)

        for j in range(m):
            if grid[0][j] == 1:
                bfs(0, j)
            if grid[n - 1][j] == 1:
                bfs(n - 1, j)

        # Count remaining land cells
        enclave_count = sum(row.count(1) for row in grid)

        return enclave_count
