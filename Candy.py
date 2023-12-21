class Solution:
    def minCandy(self, n, r):
        sum, l = 0, [1]*n
        for i in range(1, n):
            if r[i] > r[i-1]:
                l[i] = l[i-1]+1
            else:
                l[i]=1
                j=i
                while j>0 and r[j-1] > r[j] and l[j-1] <= l[j]:
                    l[j-1] = l[j]+1
                    j-=1
        
        for i in l:
            sum+=i
        return sum
