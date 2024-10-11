class Solution:
    def rearrange(self, arr):
        result = [-1] * len(arr)
        for value in arr:
            if 0 <= value < len(arr):
                result[value] = value
        return result
