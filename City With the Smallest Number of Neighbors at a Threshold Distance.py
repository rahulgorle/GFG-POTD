from typing import List

class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], d : int) -> int:
        # code here
        from collections import defaultdict
        from heapq import heappush, heappop
        g = defaultdict(list)
        
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        def dijkstr(n):
            costs = {n: 0}
            q = [(0, n)]
            while q:
                cost0, n0 = heappop(q)
                for nbr, c in g[n0]:
                    cost = cost0+c
                    if cost > d:
                        continue
                    if nbr not in costs or costs[nbr] > cost:
                        costs[nbr] = cost
                        heappush(q, (cost, nbr))
            return len(costs)
            
        ans = 0
        cnt = n
        for k in range(n):
            c = dijkstr(k)
            if c <= cnt:
                cnt = c
                ans = k
        return ans
