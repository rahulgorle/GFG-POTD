from typing import List

class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        arr.append(1e9+7)
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + (r-l+1)//2
            if arr[m] > k:
                r = m-1
            else:
                l = m
        if abs(arr[l] - k) < abs(arr[l+1] - k):
            return arr[l]
            
        return arr[l+1]
