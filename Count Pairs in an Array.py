from bisect import bisect_left
class Solution:    
    def countPairs(self, arr, n):
        ordered, count = [], 0
        for i in reversed(range(n)):
            ai = arr[i] * i
            j = bisect_left(ordered, ai)
            count += j
            ordered.insert(j, ai)
        return count
