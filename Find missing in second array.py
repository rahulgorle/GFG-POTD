class Solution:
    def findMissing(self,a,b,n,m):
        st = set(b)
        return [ele for ele in a if ele not in st]
