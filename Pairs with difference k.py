from collections import Counter
class Solution:
	def countPairsWithDiffK(self, arr, k):
    	d = Counter(arr)
        ctr = 0
        for i in arr:
            if i - k in d:
                ctr += d[i - k]
    	return ctr
