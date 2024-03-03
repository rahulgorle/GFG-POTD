from functools import cmp_to_key
class Solution:
    def printLargest(self, n, arr):
        arr = sorted(arr, key=cmp_to_key(lambda n1, n2: -1 if n1+n2 > n2+n1 else 1))
        return ''.join(arr)
