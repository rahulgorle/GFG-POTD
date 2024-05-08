class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        temp = []
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node == -1:
                temp.pop()
                continue
            temp.append(node.data)
            stack.append(-1)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not (node.left or node.right):
                ans.append(temp[:])
        return ans
