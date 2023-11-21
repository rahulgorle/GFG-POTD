class Solution:
    # Function to check if two trees are identical.
    def isIdentical(self, root1, root2):
        # Base Case: If both trees are empty, they are identical
        if not root1 and not root2:
            return True
        
        # If one of the trees is empty while the other is not, they are not identical
        if not root1 or not root2:
            return False
        
        # Using recursion to check the subtrees
        return (root1.data == root2.data and
                self.isIdentical(root1.left, root2.left) and
                self.isIdentical(root1.right, root2.right))
