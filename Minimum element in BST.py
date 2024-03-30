class Solution:
    def minValue(self, root):
        if root is None:
            return None  
        if root.left is None:
            return root.data  
        return self.minValue(root.left)
