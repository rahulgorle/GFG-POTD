class Solution:
    
    def maxStep(self, arr):
        n = len(arr)
        cnt = 0
        maxi = 0
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                cnt += 1
            else:
                maxi = max(maxi, cnt)
                cnt = 0
        maxi = max(maxi, cnt)
        return maxi
