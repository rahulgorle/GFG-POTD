class Solution:
    def removeDuplicates(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res
