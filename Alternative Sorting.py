class Solution:
    def alternateSort(self, arr):
        ans = []
        arr.sort()
        a = len(arr)
        b = a // 2
        for i in range(b):
            ans.append(arr[a - i - 1])
            ans.append(arr[i])
        if a % 2 == 1:
            ans.append(arr[b])
        return ans
