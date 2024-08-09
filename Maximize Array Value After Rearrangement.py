class Solution:
    def Maximize(self, arr): 
        l = 0
        arr.sort()
        for i in range(len(arr)):
            l += arr[i] * i
            b = l % (10 ** 9 + 7)
        return b
