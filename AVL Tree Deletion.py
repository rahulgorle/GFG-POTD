class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if node is None:
        return 0
    return node.height

def getBalanceFactor(node):
    if node is None:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))

    return x

def leftRotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = getMinValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalanceFactor(root)

    if balance > 1:
        if getBalanceFactor(root.left) >= 0:
            return rightRotate(root)
        else:
            root.left = leftRotate(root.left)
            return rightRotate(root)

    if balance < -1:
        if getBalanceFactor(root.right) <= 0:
            return leftRotate(root)
        else:
            root.right = rightRotate(root.right)
            return leftRotate(root)

    return root

def getMinValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
