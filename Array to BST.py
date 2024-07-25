class Solution:
    def sortedArrayToBST(self, nums):
        n = len(nums)
        def mergeTree(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = Node(nums[m])
            root.left = mergeTree(l, m - 1)
            root.right = mergeTree(m + 1, r)
            
            return root
        
        return mergeTree(0, n - 1)
