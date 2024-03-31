class Solution:
    def findMaxForN(self, root, n):
        find=-1
        while(root):
            if(root.key>n):
                root=root.left
            else:
                if(root.key<=n):
                    find=root.key
                    root=root.right
        return find
