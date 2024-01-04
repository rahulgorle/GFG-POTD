class Solution:
    def singleElement(self, arr, N):
        one, two = 0, 0
        for i in arr:
            one = (one ^ i) & (~two)
            two = (two ^ i) & (~one)
        return one
