class Solution:
    def isEulerCircuitExist(self, V, adj):
        in_degree = [0] * V

        # Calculate in-degree for each vertex
        for i in range(V):
            in_degree[i] = len(adj[i])

        # Count the number of vertices with odd in-degree
        odd_count = 0
        for degree in in_degree:
            if degree % 2 != 0:
                odd_count += 1

        # If there are more than two vertices with odd in-degree, return 0
        if odd_count > 2:
            return 0

        # If there are exactly two vertices with odd in-degree, it's an Eulerian path
        if odd_count == 2:
            return 1

        # If all vertices have even in-degree, it's an Eulerian circuit
        return 2
