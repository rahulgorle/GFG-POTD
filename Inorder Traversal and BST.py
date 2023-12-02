class Solution:
    def isRepresentingBST(self, arr, N):
            for i in range(N):
                if arr[i]==arr[-1]:
                    break
                if arr[i]>arr[i+1]:
                    return 0
            return 1
