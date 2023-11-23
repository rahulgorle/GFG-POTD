class Solution:
    def getHeight(self, node):
        return 0 if not node else node.height

    def updateHeight(self, node):
        if not node:
            return 0
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        return node.height

    def getBalance(self, root):
        return 0 if not root else (self.getHeight(root.left) - self.getHeight(root.right))

    def leftRotate(self, root):
        y = root.right
        t2 = y.left
        y.left = root
        root.right = t2
        self.updateHeight(root)
        self.updateHeight(y)
        return y

    def rightRotate(self, root):
        y = root.left
        t2 = y.right
        y.right = root
        root.left = t2
        self.updateHeight(root)
        self.updateHeight(y)
        return y

    def insertToAVL(self, root, key):
        if not root:
            return Node(key)

        if key == root.data:
            return root
        elif key < root.data:
            root.left = self.insertToAVL(root.left, key)
        else:
            root.right = self.insertToAVL(root.right, key)

        self.updateHeight(root)

        balance = self.getBalance(root)

        if balance > 1:
            if key < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if key > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root
