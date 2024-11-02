class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        d = {}
        for i in range(len(arr)):
            if arr[i] not in d.keys():
                d[arr[i]] = []
            d[arr[i]].append(i)    
            if (d[arr[i]][-1] - d[arr[i]][0]) <= k:
                if (d[arr[i]][-1] - d[arr[i]][0]) != 0:
                   return True
        return False
