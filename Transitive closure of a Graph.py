class Solution:
    def transitiveClosure(self, N, graph):
        # Initialize the result matrix as an identity matrix
        result = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                if i == j or graph[i][j] == 1:
                    result[i][j] = 1

        # Perform the Floyd-Warshall algorithm
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    result[i][j] = result[i][j] or (result[i][k] and result[k][j])

        return result
