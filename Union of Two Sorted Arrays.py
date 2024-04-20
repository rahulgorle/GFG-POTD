class Solution:
    def findUnion(self,arr1,arr2,n,m):
        return sorted(list(set(arr1 + arr2)))
