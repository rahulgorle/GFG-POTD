class Solution:
    def findIntersection(self, head1, head2):
        dummy = Node(0)  # Dummy node to keep track of the result list
        current = dummy

        while head1 is not None and head2 is not None:
            if head1.data == head2.data:
                current.next = Node(head1.data)
                current = current.next
                head1 = head1.next
                head2 = head2.next
            elif head1.data < head2.data:
                head1 = head1.next
            else:
                head2 = head2.next

        return dummy.next  # Return the next of the dummy node, which is the head of the result list
