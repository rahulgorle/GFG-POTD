class Solution:
    def sumOfLeafNodes(self, root):
        def sum_leaf_nodes(node):
            if not node:
                return
            if not node.left and not node.right:
                self.leaf_sum += node.data
                return


            sum_leaf_nodes(node.left)
            sum_leaf_nodes(node.right)
       
        self.leaf_sum = 0
        sum_leaf_nodes(root)
        return self.leaf_sum
