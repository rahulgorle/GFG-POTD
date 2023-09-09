class Solution:
    def kthLargest(self, root, k):
        self.kth_largest = None
        self.count = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.count += 1
            if self.count == k:
                self.kth_largest = node.data
                return
            reverse_inorder(node.left)

        reverse_inorder(root)
        return self.kth_largest
