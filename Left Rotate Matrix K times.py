class Solution:
    def rotateMatrix(self, k, mat):
        n = len(mat)
        k = k % len(mat[0])
        for i in range(n):
            mat[i] = mat[i][k:] + mat[i][:k]
        return mat
