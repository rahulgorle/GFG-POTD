class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        if not root:
            return True
        
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.data == right.data) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)
