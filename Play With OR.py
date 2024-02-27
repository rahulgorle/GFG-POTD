class Solution:
    def game_with_number (self, arr,  n) :
        res = []
        for i in range(n-1):
            res.append(arr[i]|arr[i+1])
        res.append(arr[-1])
        return res
