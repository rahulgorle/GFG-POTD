from heapq import heappush, heappop

class Solution:
    def maxIndexDiff(self, a, n):
        mx = 0
        t = [(a[i], i) for i in range(n)]
        t.sort()
        pq = [(t[0][1], t[0][0])]
        for i in range(1, n):
            idx, val = pq[0]
            currval, curridx = t[i]
            if curridx > idx:
                mx = max(mx, curridx - idx)
            heappush(pq, (t[i][1], t[i][0]))
        
        return mx
