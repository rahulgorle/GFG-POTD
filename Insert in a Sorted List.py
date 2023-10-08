class Solution:
    def sortedInsert(self, head1, key):
        new_node = Node(key)

        # Case: If the linked list is empty, make the new node the head
        if head1 is None:
            return new_node

        # Case: If the new node should be inserted at the beginning
        if key < head1.data:
            new_node.next = head1
            return new_node

        current = head1
        prev = None

        # Traverse the linked list to find the appropriate position to insert the new node
        while current and key >= current.data:
            prev = current
            current = current.next

        # Insert the new node between prev and current
        prev.next = new_node
        new_node.next = current

        return head1
