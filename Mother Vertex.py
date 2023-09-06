class Solution:
    def __init__(self):
        self.visited = None
        self.last_visited = -1

    def dfs(self, v, adj):
        self.visited[v] = True
        for neighbor in adj[v]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, adj)
        self.last_visited = v

    def findMotherVertex(self, V, adj):
        self.visited = [False] * V
        self.last_visited = -1

        for v in range(V):
            if not self.visited[v]:
                self.dfs(v, adj)

        # Reset visited array for a new traversal
        self.visited = [False] * V

        # Check if the last_visited vertex can reach all other vertices
        self.dfs(self.last_visited, adj)

        # If the last_visited vertex can reach all vertices, it's a mother vertex
        if all(self.visited):
            return self.last_visited
        else:
            return -1
