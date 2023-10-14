class Solution:
    
    # Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        common_nodes = []
        stack1, stack2 = [], []
        
        while stack1 or stack2 or root1 or root2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
                
            while root2:
                stack2.append(root2)
                root2 = root2.left
            
            if not stack1 or not stack2:
                break
            
            top1, top2 = stack1[-1], stack2[-1]
            
            if top1.data == top2.data:
                common_nodes.append(top1.data)
                stack1.pop()
                stack2.pop()
                root1 = top1.right
                root2 = top2.right
            elif top1.data < top2.data:
                stack1.pop()
                root1 = top1.right
            else:
                stack2.pop()
                root2 = top2.right
        
        return common_nodes
