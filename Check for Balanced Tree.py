class Solution:
    def isBalanced(self, root):
        def is_balanced_helper(node):
            if node is None:
                return True, 0

            left_balanced, left_height = is_balanced_helper(node.left)
            right_balanced, right_height = is_balanced_helper(node.right)

            is_current_balanced = abs(left_height - right_height) <= 1
            is_tree_balanced = left_balanced and right_balanced and is_current_balanced
            tree_height = max(left_height, right_height) + 1

            return is_tree_balanced, tree_height

        is_balanced, _ = is_balanced_helper(root)
        return is_balanced
