class Solution:
    def is_sum_tree(self, node):
        # Helper function that returns a tuple (is_sum_tree, sum)
        def check_sum_tree(node):
            if node is None:
                return True, 0
            
            if node.left is None and node.right is None:
                return True, node.data
            
            left_is_sum_tree, left_sum = check_sum_tree(node.left)
            right_is_sum_tree, right_sum = check_sum_tree(node.right)
            
            # Check if current node is sum tree
            current_is_sum_tree = (left_is_sum_tree and right_is_sum_tree and 
                                   node.data == left_sum + right_sum)
            
            # Return whether this subtree is a sum tree and the sum of this subtree
            return current_is_sum_tree, left_sum + right_sum + node.data
        
        # Only need the boolean result from the helper function
        is_sum_tree, _ = check_sum_tree(node)
        return is_sum_tree
