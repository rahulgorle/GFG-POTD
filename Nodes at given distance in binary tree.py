class Solution:
    
    def KDistanceNodes(self, root, target, k):
        def findTarget(node, target):
            # Helper function to find the target node in the tree
            if not node:
                return None
            if node.data == target:
                return node
            left = findTarget(node.left, target)
            if left:
                return left
            return findTarget(node.right, target)
        
        def findKDistanceNodes(node, k, result):
            # Helper function to find nodes at distance k from the target node
            if not node or k < 0:
                return
            if k == 0:
                result.append(node.data)
                return
            findKDistanceNodes(node.left, k - 1, result)
            findKDistanceNodes(node.right, k - 1, result)
        
        targetNode = findTarget(root, target)
        result = []
        def dfs(node, k):
            if not node:
                return -1
            if node == targetNode:
                findKDistanceNodes(node, k, result)
                return 0
            left_dist = dfs(node.left, k)
            right_dist = dfs(node.right, k)
            
            if left_dist >= 0:
                if left_dist + 1 == k:
                    result.append(node.data)
                else:
                    findKDistanceNodes(node.right, k - left_dist - 2, result)
                return left_dist + 1
            elif right_dist >= 0:
                if right_dist + 1 == k:
                    result.append(node.data)
                else:
                    findKDistanceNodes(node.left, k - right_dist - 2, result)
                return right_dist + 1
            return -1
        
        dfs(root, k)
        return sorted(result)
