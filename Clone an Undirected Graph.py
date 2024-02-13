class Solution():
    def cloneGraph(self, node):
        
        # Fix for judge's code doing to many recursion calls
        import sys
        sys.setrecursionlimit(10**4)
        # end of fix
        
        # N leeks from the judge's code
        #N = 10**4
        nodes = [Node(i, []) for i in range(N)]
        visited = [False] * N
        s = [node]
        while s:
            u = s.pop()
            if visited[u.val]:
                continue
            visited[u.val] = True
            copy_u = nodes[u.val]
            for v in u.neighbors:
                copy_u.neighbors.append(nodes[v.val])
                if not visited[v.val]:
                    s.append(v)
        return nodes[node.val]
