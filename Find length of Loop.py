class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                count = 1
                while slow.next!=fast:
                    count+=1
                    slow=slow.next
                return count
        return 0
