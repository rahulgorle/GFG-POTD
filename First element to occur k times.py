class Solution:
    def firstElementKTime(self, n, k, a):
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]>=k:
                return i
        return -1
