class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        if not head:
            new_node.next = new_node
            return new_node

        if head.data >= data:
            curr = head
            while curr.next != head:
                curr = curr.next
            new_node.next, curr.next = head, new_node
            return new_node
        else:
            curr = head
            while curr.next.data < data and curr.next != head:
                curr = curr.next
            new_node.next, curr.next = curr.next, new_node
            return head
