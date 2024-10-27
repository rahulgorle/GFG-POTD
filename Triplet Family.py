class Solution:
    def findTriplet(self, arr):
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if (arr[i] + arr [j]) in arr:
                    return True
                elif (arr[i] + arr [j]) > arr[-1]:
                    j = len(arr)
                    
        return False
