def insert(head, data):
    node = Node(data)
    if head == None: head = node
    else:
        node.npx = head
        head = node
    return head
    
def getList(head):
    lis = []
    while head:
        lis.append(head.data)
        head = head.npx
    return lis
