class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Your code here
        res=[]
        level=[root]
        flag=False
        while level:
            next=[]
            while level:
                top=level.pop()
                res.append(top.data)
                if flag:
                    if top.right:
                        next.append(top.right)
                    if top.left:
                        next.append(top.left)
                else:
                    if top.left:
                        next.append(top.left)
                    if top.right:
                        next.append(top.right)
            level=next
            flag=not flag
        return res
