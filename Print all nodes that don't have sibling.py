def noSibling(root):
    list = []
    def sibling(root,list):
        if root == None:
            return
        if (root.left == None and root.right != None):
            list.append(root.right.data)
        elif (root.left != None and root.right == None):
            list.append(root.left.data)
        sibling(root.left,list)
        sibling(root.right,list)
        return list
    sibling(root,list)
    if len(list) == 0:
        list.append(-1)
    return sorted(list)
