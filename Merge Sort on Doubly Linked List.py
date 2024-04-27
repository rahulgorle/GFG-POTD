class Solution():
    def sortDoubly(self,head):
        lis = []
        while head:
            lis.append(head.data)
            head = head.next
        lis.sort()
        root = Node(lis[0])
        cur = root
        for i in lis[1:]:
            cur.next = Node(i)
            cur.next.prev = cur
            cur = cur.next
        return root
