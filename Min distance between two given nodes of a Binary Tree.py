class Solution:
    def findDist(self, root, node_val_1, node_val_2):
        def distance_to_node(node, target):
            if not node:
                return -1
            if node.data == target:
                return 0

            left_distance = distance_to_node(node.left, target)
            right_distance = distance_to_node(node.right, target)

            if left_distance >= 0:
                return left_distance + 1
            if right_distance >= 0:
                return right_distance + 1

            return -1

        def lowest_common_ancestor(node, node_val_1, node_val_2):
            if not node:
                return None
            if node.data == node_val_1 or node.data == node_val_2:
                return node

            left_lca = lowest_common_ancestor(node.left, node_val_1, node_val_2)
            right_lca = lowest_common_ancestor(node.right, node_val_1, node_val_2)

            if left_lca and right_lca:
                return node
            return left_lca if left_lca else right_lca

        lca_node = lowest_common_ancestor(root, node_val_1, node_val_2)
        return distance_to_node(lca_node, node_val_1) + distance_to_node(lca_node, node_val_2)
