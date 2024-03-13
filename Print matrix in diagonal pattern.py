class Solution:
    def matrixDiagonally(self,mat):
        n , res = len(mat), []
        for i in range(2*n - 1):
            extra = i - n + 1
            if i % 2 == 0:
                row , col = i if extra <= 0 else n - 1, 0 if extra <= 0 else extra
                while row >= 0 and col < n:
                    res.append(mat[row][col])
                    row, col = row - 1, col + 1
            else:
                row , col = 0 if extra <= 0 else extra, i if extra <= 0 else n - 1
                while row < n and col >= 0:
                    res.append(mat[row][col])
                    row, col = row + 1, col - 1
        return res
