def ancestors(root,target,arr):
    if(root==None):
        return False
    if(root.data==target):
        return True
    l = ancestors(root.left, target, arr)
    r = ancestors(root.right, target, arr)
    if(l or r):
        arr.append(root.data)
        
    return l or r


class Solution:

    def Ancestors(self, root, target):
        arr = []
        ancestors(root,target,arr)
        return arr
