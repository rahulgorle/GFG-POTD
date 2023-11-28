class Solution:
    def sumOfDependencies(self, adj, V):
        total_dependencies = 0
        
        for node in range(V):
            total_dependencies += len(adj[node])
        
        return total_dependencies
