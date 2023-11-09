class Solution:
    def columnWithMaxZeros(self, arr, N):
        max_zeros = 0
        max_zeros_column = -1

        for j in range(N):
            zeros_count = 0
            for i in range(N):
                if arr[i][j] == 0:
                    zeros_count += 1

            if zeros_count > max_zeros:
                max_zeros = zeros_count
                max_zeros_column = j

        return max_zeros_column
