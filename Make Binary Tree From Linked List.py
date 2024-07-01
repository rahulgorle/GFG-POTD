def convert(head):
    arr = []
    while head:
        arr.append(head.data)
        head = head.next
    
    def fun(arr, i):
        if i >= len(arr):
            return None
        
        root = Tree(arr[i])
        root.left = fun(arr, 2 * i + 1)
        root.right = fun(arr, 2 * i + 2)
        
        return root
    
    return fun(arr, 0)
