class Solution:
    def ans(self, ptr, target, maxtime):
        if ptr is None:
            return 0
        
        val_1 = self.ans(ptr.left, target, maxtime)
        val_2 = self.ans(ptr.right, target, maxtime)
        
        if ptr.data == target:
            maxtime[0] = max(maxtime[0], max(val_1, val_2))
            return -1
        
        if val_1 >= 0 and val_2 >= 0:
            return max(val_1, val_2) + 1
        
        if val_1 > val_2:
            val_1, val_2 = val_2, val_1
        
        maxtime[0] = max(maxtime[0], val_2 - val_1)
        return val_1 - 1

    def minTime(self, root, target):
        maxtime = [0]
        self.ans(root, target, maxtime)
        return maxtime[0]
