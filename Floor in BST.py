class Solution:
    def floor(self, root, x):
        floor_value = -1  # Initialize the floor value to -1

        while root is not None:
            if root.data == x:
                return x  # x is found in the tree, return it as the floor value
            elif root.data < x:
                floor_value = root.data  # Update the floor value
                root = root.right  # Move to the right subtree
            else:
                root = root.left  # Move to the left subtree

        return floor_value  # Return the final floor value
