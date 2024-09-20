class Solution:
    def countBuildings(self, height):
        n = len(height)
        h = height[0]
        count = 1
        for i in range(1, n):
            if height[i] > h:
                count += 1
                h = height[i]
        return count
