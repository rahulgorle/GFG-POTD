from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Helper function to perform DFS to find the size of an island
        def dfs(x, y, color):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = color
            size = 1
            size += dfs(x + 1, y, color)
            size += dfs(x - 1, y, color)
            size += dfs(x, y + 1, color)
            size += dfs(x, y - 1, color)
            return size

        # Initialize the color for each island
        color = 2
        island_sizes = {}  # A dictionary to store island sizes based on their colors

        # Traverse the grid and label each island with a unique color
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size = dfs(i, j, color)
                    island_sizes[color] = island_size
                    color += 1

        # Initialize the maximum island size to 0
        max_island_size = max(island_sizes.values()) if island_sizes else 0

        # Iterate through the grid and try changing each 0 to 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_colors = set()
                    if i > 0:
                        neighbor_colors.add(grid[i - 1][j])
                    if i < n - 1:
                        neighbor_colors.add(grid[i + 1][j])
                    if j > 0:
                        neighbor_colors.add(grid[i][j - 1])
                    if j < n - 1:
                        neighbor_colors.add(grid[i][j + 1])

                    island_size_with_new_1 = 1  # Size of island if we change this 0 to 1
                    for neighbor_color in neighbor_colors:
                        if neighbor_color != 0:
                            island_size_with_new_1 += island_sizes[neighbor_color]

                    max_island_size = max(max_island_size, island_size_with_new_1)

        return max_island_size
