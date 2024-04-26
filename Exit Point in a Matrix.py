class Solution:
	def FindExitPoint(self, n, m, mat):
	    i,j,d=0,0,0
        while (0<=i<n and 0<=j<m):
            if mat[i][j]==1:
                mat[i][j]=0
                d=(d+1)%4
            if d==0: #Move downwards
                j+=1
            elif d==1: #Move forward towards right
                i+=1
            elif d==2: # Move upwards
                j-=1
            else: #Move forward towards left
                i-=1
        if d==0: return (i,j-1)
        elif d==1: return (i-1,j)
        elif d==2: return (i,j+1)
        return (i+1,j)
