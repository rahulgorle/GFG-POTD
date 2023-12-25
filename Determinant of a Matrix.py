class Solution:
    def determinantOfMatrix(self,matrix,n):
        if n==1:
            return matrix[0][0]
        if n==2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            det = 0
            for i in range(n):
                if i%2 == 0:
                    flag = 1
                else:
                    flag = -1
                mat = [row[0:i] + row[i+1:] for row in matrix[1:]]
                det += flag*matrix[0][i]*self.determinantOfMatrix(mat, n-1)
            return det
