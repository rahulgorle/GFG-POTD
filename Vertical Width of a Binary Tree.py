def verticalWidth(root):
    if root is None:
        return 0
    
    def dfs(node, hd, hd_set):
        if node is None:
            return
        
        hd_set.add(hd)
        
        
        if node.left:
            dfs(node.left, hd - 1, hd_set)
        if node.right:
            dfs(node.right, hd + 1, hd_set)
    
    
    hd_set = set()
    dfs(root, 0, hd_set)
    
    return len(hd_set)
