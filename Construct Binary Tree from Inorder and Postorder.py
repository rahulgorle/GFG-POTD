class Solution:
    def buildTree(self, In, post, n):
        if not In or not post:
            return 
        index = In.index(post[-1])
        root = Node(post[-1])
        root.left = self.buildTree(In[0:index],post[0:index],n)
        root.right = self.buildTree(In[index+1:],post[index:-1],n)
        return root
