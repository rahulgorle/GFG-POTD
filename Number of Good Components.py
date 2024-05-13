from typing import List
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, e: int, v: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for fm, to in edges:
            adj[fm].add(to)
            adj[to].add(fm)

        seen = set()
        constituent = defaultdict(set)
        minimum = defaultdict(lambda: float('inf'))

        def fill(root, cur):
            nonlocal adj, seen, constituent
            if cur in seen:
                return
            constituent[root].add(cur)
            minimum[root] = min(minimum[root], len(adj[cur]))
            seen.add(cur)
            for to in adj[cur] - seen:
                fill(root, to)

        for cur in range(1, v + 1):
            fill(cur, cur)

        return sum(1 for root in constituent if minimum[root] == len(constituent[root]) - 1)
