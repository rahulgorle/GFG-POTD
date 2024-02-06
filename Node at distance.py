class Solution:
    def __init__(self):
        self.result = 0

    def printKDistantfromLeaf(self, root, k):
        def dfs(node, path):
            nonlocal result
            if not node:
                return
            path.append(node)
            if not node.left and not node.right:  # Leaf node
                if len(path) > k:
                    result.add(path[-k - 1])  # Adding the node itself
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        result = set()
        dfs(root, [])
        return len(result)
