from collections import deque

# Node Class:
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to find the height of a binary tree.
    def height(self, root):
        if root is None:
            return 0
        
        # Using level order traversal (BFS) to find the height of the tree
        queue = deque()
        queue.append(root)
        height = 0
        
        while queue:
            # Process all nodes at the current level
            node_count = len(queue)
            
            for i in range(node_count):
                current_node = queue.popleft()
                
                # Enqueue the left child if it exists
                if current_node.left:
                    queue.append(current_node.left)
                
                # Enqueue the right child if it exists
                if current_node.right:
                    queue.append(current_node.right)
            
            # Increment the height after processing each level
            height += 1
        
        return height
