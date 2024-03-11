class Solution:
	def front(self,n,i,j):
        if j==n-1:
            i+=1
            j=0
        else:
            j+=1
        return i,j
    
    def rear(self,n,i,j):
        if j==0:
            i-=1
            j=n-1
        else:
            j-=1
        return i,j
    
    
    def is_valid(self,n,i,j,a,b):
        if i==n:
            return False
        if a==-1:
            return False
        return True
    
    def countPairs(self, mat1, mat2, n, x):
        i,j,a,b=0,0,n-1,n-1
        count=0
        while self.is_valid(n,i,j,a,b):
            sum=mat1[i][j]+mat2[a][b]
            if sum==x:
                count+=1
                i,j=self.front(n,i,j)
                a,b=self.rear(n,a,b)
            elif sum>x:
                a,b=self.rear(n,a,b)
            else:
                i,j=self.front(n,i,j)
        return count
