class Solution:
    def binaryTreeToBST(self, root):
        
        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.data] + inorder(root.right)
        
        def io(root):
            nonlocal i
            if not root: return
            io(root.left)
            if root:
                root.data = ls[i]
                i += 1
            io(root.right)
        
        ls = inorder(root)
        ls.sort()
        i = 0
        io(root)
