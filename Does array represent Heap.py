class Solution:
    def isMaxHeap(self,arr,n):
        for i in range(n//2):
            if i==n//2-1:
                if arr[i]<arr[i*2+1]:
                    return 0
            elif arr[i] < arr[i*2+1] or arr[i]< arr[i*2+2]:
                return 0
        return 1
