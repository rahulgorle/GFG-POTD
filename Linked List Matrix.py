class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        flag=0
        n=len(mat)
        for i in range(n):
            f1=0
            for j in range(n):
                if not flag:
                    head=Node(mat[i][j])
                    flag=1
                    cur=head
                if i+1<n:
                    cur.down=Node(mat[i+1][j])
                if j+1<n:
                    cur.right=Node(mat[i][j+1])
                if not f1:
                    temp=cur
                    f1=1
                cur=cur.right
            cur=temp.down
        return head
