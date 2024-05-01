class Solution:
    def arrangeCV(self, head):
        vowels = ["a", "e","i","o", "u"]
        dummy = Node(-1)
        dummy.next = head
        vow = dummy
        prev= dummy
        curr = head 
        
        while(curr):
            if curr.data in vowels:
                del_node =  curr
                prev.next = curr.next
                curr = prev.next
                nxt = vow.next
                vow.next = del_node
                del_node.next =  nxt
                vow = del_node
                if vow.next == curr:
                    prev = vow
            else:
                curr = curr.next
                prev = prev.next 
        return dummy.next
