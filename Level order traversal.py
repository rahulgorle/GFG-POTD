class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        queue = deque([root])
        traversal = []
        
        while queue:
            node = queue.popleft()
            traversal.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return traversal
