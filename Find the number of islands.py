class Solution:
    def numIslands(self, grid):
        def f(i, j, vis):
            # Check the 8 possible directions
            for r, c in [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, 1], [1, -1], [1, 1], [-1, -1]]:
                nr, nc = i + r, j + c
                # Continue the DFS if the new coordinates are valid and not visited
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in vis and grid[nr][nc] != 0:
                    vis.add((nr, nc))
                    f(nr, nc, vis)

        cnt, vis = 0, set()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in vis:
                    cnt += 1
                    vis.add((i, j))
                    f(i, j, vis)

        return cnt
