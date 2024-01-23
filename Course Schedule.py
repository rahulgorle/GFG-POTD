class Solution:
    def findOrder(self, n, m, prerequisites):
        # Initialize in-degrees and adjacency list
        in_degree = [0] * n
        graph = [[] for _ in range(n)]
        
        # Build the in-degrees and adjacency list
        for edge in prerequisites:
            in_degree[edge[0]] += 1
            graph[edge[1]].append(edge[0])
        
        # Initialize result order
        order = []
        
        # Perform BFS
        queue = [i for i in range(n) if in_degree[i] == 0]
        for node in queue:
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all tasks are visited
        if len(order) != n:
            return []
        else:
            return order
