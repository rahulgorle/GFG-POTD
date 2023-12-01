class Solution:
    def isDeadEnd(self, root):
        def isDeadEndHelper(node, min_val, max_val):
            if not node:
                return False

            if min_val == max_val:
                return True

            left = isDeadEndHelper(node.left, min_val, node.data - 1)
            right = isDeadEndHelper(node.right, node.data + 1, max_val)

            return left or right

        return isDeadEndHelper(root, 1, float('inf'))
