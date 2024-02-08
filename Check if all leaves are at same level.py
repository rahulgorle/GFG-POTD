class Solution:
    def check(self, root):
        # Set to store levels of leaf nodes
        leaf_levels = set()
       
        # Helper function to traverse tree and record leaf levels
        def traverse(node, level):
            if not node:
                return
            if not node.left and not node.right:
                leaf_levels.add(level)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
       
        # Start traversal from root at level 0
        traverse(root, 0)
       
        # If all leaf nodes are at the same level, return True, else False
        return len(leaf_levels) == 1

