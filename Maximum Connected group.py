from typing import List

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        
        def dfs(x, y, index):
            stack = [(x, y)]
            component_size = 0
            while stack:
                cx, cy = stack.pop()
                if visited[cx][cy]:
                    continue
                visited[cx][cy] = True
                component_size += 1
                component_map[cx][cy] = index
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                        stack.append((nx, ny))
            return component_size
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        component_map = [[-1] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        component_sizes = []
        
        # Step 1: Identify all connected components of 1's
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    component_size = dfs(i, j, len(component_sizes))
                    component_sizes.append(component_size)
        
        if not component_sizes:
            return 1
        
        max_connection = max(component_sizes)  # Initial max connection without any change
        
        # Step 2: For each 0 in the grid, calculate potential max size if changed to 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_components = set()
                    potential_size = 1  # Changing (i, j) to 1
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            neighbor_components.add(component_map[ni][nj])
                    for comp in neighbor_components:
                        potential_size += component_sizes[comp]
                    max_connection = max(max_connection, potential_size)
        
        return max_connection
