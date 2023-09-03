class Solution:
    # Return True if the given trees are isomorphic. Else return False.
    def isIsomorphic(self, root1, root2):
        # If both trees are None, they are isomorphic
        if not root1 and not root2:
            return True

        # If one tree is None but the other is not, they are not isomorphic
        if (not root1 and root2) or (root1 and not root2):
            return False

        # Recursively check if the root nodes and their subtrees are isomorphic
        return (root1.data == root2.data and
                ((self.isIsomorphic(root1.left, root2.left) and
                  self.isIsomorphic(root1.right, root2.right)) or
                 (self.isIsomorphic(root1.left, root2.right) and
                  self.isIsomorphic(root1.right, root2.left))))
