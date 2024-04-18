class Solution:
    def twoRepeated(self, arr, n):
        seen = {}
        result = []
        for num in arr:
            if num in seen:
                if seen[num] == 1:
                    result.append(num)
                seen[num] += 1
            else:
                seen[num] = 1
        return result
