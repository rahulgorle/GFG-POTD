class Solution:
    def countPairs(self, root1, root2, x):
        stack1, stack2 = [], []
        curr1, curr2 = root1, root2
        count = 0

        while (curr1 or stack1) or (curr2 or stack2):
            while curr1:
                stack1.append(curr1)
                curr1 = curr1.left

            while curr2:
                stack2.append(curr2)
                curr2 = curr2.right

            if not stack1 or not stack2:
                break

            top1, top2 = stack1[-1], stack2[-1]

            if top1.data + top2.data == x:
                count += 1
                stack1.pop()
                stack2.pop()
                curr1 = top1.right
                curr2 = top2.left
            elif top1.data + top2.data < x:
                stack1.pop()
                curr1 = top1.right
            else:
                stack2.pop()
                curr2 = top2.left

        return count
