class Solution:
    def insertionSort(self, head):
        # Check if the linked list is empty or has only one element
        if not head or not head.next:
            return head

        # Initialize pointers and a dummy node
        previous_node, current_node_to_insert = None, None
        dummy_head = Node(-1)
        dummy_head.next = head

        # Traverse the linked list
        while head and head.next:
            # If the current node's value is less than or equal to the next node's value, move to the next node
            if head.data <= head.next.data:
                head = head.next
            else:
                # Set pointers to the dummy node and the node to be inserted
                previous_node, current_node_to_insert = dummy_head, head.next

                # Find the correct position for insertion
                while previous_node.next.data < current_node_to_insert.data:
                    previous_node = previous_node.next

                # Update pointers to perform the insertion
                head.next = head.next.next
                current_node_to_insert.next = previous_node.next
                previous_node.next = current_node_to_insert

        # Return the sorted linked list starting from the dummy node
        return dummy_head.next
