class Solution:
    def leafNodesByLevel(self, node, level):
        """
        Helper function to find leaf nodes with their levels.
        """
        if node is None:
            return []
        
        if node.left is None and node.right is None:
            return [(node.data, level)]
        
        left_leaves = self.leafNodesByLevel(node.left, level + 1)
        right_leaves = self.leafNodesByLevel(node.right, level + 1)
        
        return left_leaves + right_leaves
    
    def getCount(self, root, budget):
        """
        Main function to maximize the count of visited leaf nodes within the budget.
        """
        leaves_with_levels = self.leafNodesByLevel(root, 1)
        
        # Sort the leaf nodes by their levels in ascending order
        leaves_with_levels.sort(key=lambda x: x[1])
        
        visited_leaves = 0
        
        for data, level in leaves_with_levels:
            # Calculate the cost of visiting this leaf node
            cost = level
            
            if cost <= budget:
                # If the cost is within the budget, visit this leaf node
                visited_leaves += 1
                budget -= cost
            else:
                # If the cost exceeds the budget, break the loop
                break
        
        return visited_leaves
