class Solution:
    def buildBalancedTree(self, root):
        def sorted_list_to_bst(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            mid_node = sorted_elements[mid]

            new_node = Node(mid_node.data)
            new_node.left = sorted_list_to_bst(start, mid - 1)
            new_node.right = sorted_list_to_bst(mid + 1, end)

            return new_node

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                sorted_elements.append(node)
                inorder_traversal(node.right)

        sorted_elements = []
        inorder_traversal(root)
        n = len(sorted_elements)
        new_root = sorted_list_to_bst(0, n - 1)

        return new_root
