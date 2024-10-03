class Solution:
    def findMajority(self, nums):
        from collections import Counter
        s = Counter(nums)
        q = len(nums)
        a = q / 3
        p = []
        for i in s.keys():
            if s[i] > a:
                p.append(i)
        return p if p else [-1]
