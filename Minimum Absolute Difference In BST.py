class Solution:
    def absolute_diff(self,root):
        res=[]
        def fun(root):
            nonlocal res 
            if root : res.append(root.data)
            if root.left : fun(root.left)
            if root.right : fun(root.right)
            
        fun(root)
        res.sort()
        ans = float('inf')
        for i in range(1, len(res)):
            ans = min(ans , res[i]- res[i-1])
        return ans
