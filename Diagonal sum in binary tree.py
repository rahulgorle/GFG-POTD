class Solution:
    #Complete the function below
    def diagonalSum(self, root):
        min_level, max_level = 0, 0
        level_sums = {}  # Dictionary to store sums at each level
        queue = deque()
        queue.append([root, 0])  # Adding root node with level 0 to the queue
    
        while queue:
            node, level = queue.popleft()
            level_sums[level] = level_sums.get(level, 0) + node.data
            min_level, max_level = min(min_level, level), max(max_level, level)
            if node.left: queue.append([node.left, level - 1])  # Adding left child with level decreased by 1
            if node.right: queue.append([node.right, level])  # Adding right child with same level
    
        # Returning diagonal sums from max level to min level
        return [level_sums[i] for i in range(max_level, min_level - 1, -1)]
