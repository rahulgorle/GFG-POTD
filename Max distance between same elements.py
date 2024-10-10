class Solution:
    def maxDistance(self, arr):
        mp = {}
        for i in range(len(arr)):
            if arr[i] in mp:
                mp[arr[i]] = [mp[arr[i]][0], i]
            else:
                mp[arr[i]] = [i, 0]
                
        mx = 0
        for k, v in mp.items():
            mx = max(v[1] - v[0], mx)
        return mx
