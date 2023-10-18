from typing import List

class Solution:
    def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
        def is_safe(node, visited):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1  # Mark the node as visiting

            for neighbor in adj[node]:
                if not is_safe(neighbor, visited):
                    return False

            visited[node] = 2  # Mark the node as safe
            return True

        result = []
        visited = [0] * V  # 0: not visited, 1: visiting, 2: safe

        for node in range(V):
            if is_safe(node, visited):
                result.append(node)

        return sorted(result)
