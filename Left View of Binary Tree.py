def helper(root, d, level):
    if root == None: return
    if level not in d:
        d[level] = root.data
    helper(root.left, d, level + 1)
    helper(root.right, d, level + 1)

def LeftView(root):
    d = dict()
    helper(root, d, 0)
    return [d[key] for key in d]
