from collections import deque

class Solution:
    
    # Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        visited = [False] * V
        level = [0] * V
        queue = deque()
        queue.append(0)
        visited[0] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    level[v] = level[u] + 1
                    queue.append(v)
                    if v == X:
                        return level[v]
        
        return -1
