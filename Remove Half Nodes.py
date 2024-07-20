import sys
sys.setrecursionlimit(10**5)

class Solution:
    def RemoveHalfNodes(self, node):
        inorder = []
        
        def DFS(root):
            if root is None:
                return
            DFS(root.left)
            
            if root.left is None and root.right is not None:
                pass
            elif root.right is None and root.left is not None:
                pass
            else:
                nonlocal inorder
                inorder.append(root.data)
            
            DFS(root.right)
        
        DFS(node)
        prev = n = Node(inorder.pop())
        while inorder:
            data = inorder.pop()
            node = Node(data)
            prev.left = node
            prev = node
        return n
