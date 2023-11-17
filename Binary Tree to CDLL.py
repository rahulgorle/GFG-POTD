class Solution:
    # Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        def helper(node):
            nonlocal head, prev
            if not node:
                return
            
            # Recursively convert the left subtree
            helper(node.left)
            
            # If head is not set, set it to the leftmost node
            if not head:
                head = node
            else:
                # Make the right pointer of the previous node point to the current node
                prev.right = node
                # Make the left pointer of the current node point to the previous node
                node.left = prev
            
            # Update the previous node to the current node
            prev = node
            
            # Recursively convert the right subtree
            helper(node.right)
        
        if not root:
            return None
        
        head, prev = None, None
        helper(root)
        
        # Make the head and tail pointers of the circular doubly linked list point to each other
        head.left = prev
        prev.right = head
        
        return head
