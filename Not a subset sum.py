class Solution:
    def findSmallest(self, arr):
        num = 1
        for i in arr:
            if i > num:
                return num
            num += i
        return num
