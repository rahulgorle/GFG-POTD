from collections import deque

class Solution:
    def bottomView(self, root):
        ans = deque([(root.data, 0)])
        left_bound, right_bound = 0, 0
        
        if root == None:
            return ans
        
        def traverse(node, d, p):
            nonlocal ans, left_bound, right_bound
            
            if node == None:
                return
            
            if p < left_bound:
                left_bound = p
                ans.appendleft((node.data, d))
            elif p > right_bound:
                right_bound = p
                ans.append((node.data, d))
            elif ans[p - left_bound][1] <= d:    
                ans[p - left_bound] = (node.data, d)
            
            traverse(node.left, d + 1, p - 1)
            traverse(node.right, d + 1, p + 1)
        
        traverse(root, 0, 0)
        return [i[0] for i in ans]
