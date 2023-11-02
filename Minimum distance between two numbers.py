class Solution:
    def minDist(self, arr, n, x, y):
        if x == y:
            return 0  # If both elements are the same, distance is zero.
        
        min_distance = float('inf')
        last_x_index = -1
        last_y_index = -1
        
        for i in range(n):
            if arr[i] == x:
                if last_y_index != -1:
                    min_distance = min(min_distance, i - last_y_index)
                last_x_index = i
            elif arr[i] == y:
                if last_x_index != -1:
                    min_distance = min(min_distance, i - last_x_index)
                last_y_index = i
        
        if min_distance == float('inf'):
            return -1  # If either x or y doesn't exist in the array.
        
        return min_distance
