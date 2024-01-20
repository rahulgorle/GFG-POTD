class Solution:
    def __init__(self):
        self.total_moves = 0

    def distributeCandy(self, root):
        def distribute_helper(node):
            if not node:
                return 0

            left_count = distribute_helper(node.left)
            right_count = distribute_helper(node.right)

            self.total_moves += abs(left_count) + abs(right_count)

            return left_count + node.data + right_count - 1

        distribute_helper(root)
        return self.total_moves
