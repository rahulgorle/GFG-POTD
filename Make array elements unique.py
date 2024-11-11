class Solution:
    def minIncrements(self, arr): 
        arr.sort()
        cnt = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                cnt += arr[i - 1] + 1 - arr[i]
                arr[i] = arr[i - 1] + 1
        return cnt
